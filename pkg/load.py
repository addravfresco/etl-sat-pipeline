"""
load.py

Motor de Persistencia Masiva y Carga Idempotente (Upsert).
Implementa de-duplicación interna por lote y validación contra tabla destino
para garantizar integridad referencial en cargas masivas de alto volumen.
"""
import polars as pl
from sqlalchemy import create_engine, text
from pkg.config import get_connection_string

# Inicializamos el motor SQLAlchemy con fast_executemany para máximo rendimiento en SQL Server
engine = create_engine(get_connection_string(), fast_executemany=True)

def upload_to_sql_blindado(df: pl.DataFrame, table_name: str, anexo_id: str) -> None:
    """
    Ejecuta una carga masiva hacia SQL Server con limpieza de duplicados en el origen
    y validación de existencia en el destino.
    """
    if df.is_empty():
        return

    stg_table = f"STG_{table_name}"

    # 1. Asegurar limpieza de Staging
    with engine.begin() as conn:
        conn.execute(text(f"IF OBJECT_ID('{stg_table}', 'U') IS NOT NULL TRUNCATE TABLE {stg_table};"))

    # 2. Volcado Masivo a Staging (Se lleva la columna FilaOrigen temporalmente)
    df.write_database(
        table_name=stg_table,
        connection=engine,
        if_table_exists="replace",
        engine="sqlalchemy"
    )

    # 3. Operación de Upsert con De-duplicación Interna
    with engine.begin() as conn:
        
        # Filtramos FilaOrigen para NO intentar insertarla en la tabla final
        cols_destino = [col for col in df.columns if col != "FilaOrigen"]
        columnas_insert = ", ".join([f"[{col}]" for col in cols_destino])
        
        if anexo_id == "1A":
            # De-duplicación por UUID para Anexo 1A
            # Ordenamos por FilaOrigen para que, si hay repetidos, siempre elija el primero determinísticamente
            upsert_query = f"""
                INSERT INTO {table_name} ({columnas_insert})
                SELECT {columnas_insert} FROM (
                    SELECT *, ROW_NUMBER() OVER (PARTITION BY [UUID] ORDER BY [FilaOrigen] ASC) as rn
                    FROM {stg_table}
                ) AS Stg
                WHERE rn = 1
                AND NOT EXISTS (
                    SELECT 1 FROM {table_name} AS Dest 
                    WHERE Dest.UUID = Stg.UUID
                );
            """
        
        elif anexo_id == "2B":
            # De-duplicación por HashID calculado para Anexo 2B
            # INYECCIÓN DEL BOOKMARK: Agregamos [FilaOrigen] al HASHBYTES para asegurar fidelidad del SAT
            upsert_query = f"""
                WITH CalculoHash AS (
                    SELECT 
                        CONVERT(VARCHAR(64), HASHBYTES('SHA2_256', CONCAT([UUID], '|', [ConceptoClaveProdServ], '|', [ConceptoImporte], '|', [FilaOrigen])), 2) as NewHash,
                        *
                    FROM {stg_table}
                ),
                Unicos AS (
                    SELECT *, ROW_NUMBER() OVER (PARTITION BY NewHash ORDER BY [FilaOrigen] ASC) as rn
                    FROM CalculoHash
                )
                INSERT INTO {table_name} ([HashID], {columnas_insert})
                SELECT NewHash, {columnas_insert}
                FROM Unicos
                WHERE rn = 1
                AND NOT EXISTS (
                    SELECT 1 FROM {table_name} AS Dest 
                    WHERE Dest.HashID = Unicos.NewHash
                );
            """

        conn.execute(text(upsert_query))
        
        # 4. Limpieza final
        conn.execute(text(f"IF OBJECT_ID('{stg_table}', 'U') IS NOT NULL DROP TABLE {stg_table};"))