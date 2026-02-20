"""
enforcer.py

Módulo de Integridad Estructural y Tipado (Schema Enforcement).
Garantiza que el DataFrame cumpla estrictamente con el contrato (DDL) de SQL Server,
aplicando Safe Casting y truncamiento dinámico para prevenir colapsos en la base de datos.
"""
from typing import Any, Dict
import polars as pl

# Catálogo de longitudes máximas fundamentado en el DDL de SQL Server.
# Actúa como barrera contra errores de truncamiento (String Truncation Errors).
LIMITES_LONGITUD = {
    "UUID": 36,
    "EMISORRFC": 13,
    "RECEPTORRFC": 13,
    "MONEDA": 10,
    "TIPOCAMBIO": 10,
    "TIPODECOMPROBANTE": 10,
    "SERIE": 50,
    "FOLIO": 50,
    "FORMAPAGO": 5,
    "METODOPAGO": 5,
    "CONCEPTONOIDENTIFICACION": 100,
    "CONCEPTOCLAVEPRODSERV": 20,
    "CONCEPTOUNIDAD": 50,
    "CONCEPTODESCRIPCION": 1000,
    # Límites de seguridad para campos VARCHAR(MAX) del Anexo 1A
    "NOCERTIFICADO": 500,
    "CONDICIONESDEPAGO": 500,
    "LUGAREXPEDICION": 500,
    "EMISORREGIMENFISCAL": 250,
    "RECEPTORNOMBRE": 500,
    "EMISORNOMBRE": 500
}


def estandarizar_nombres_columnas(df: pl.DataFrame) -> pl.DataFrame:
    """
    Sanitiza los identificadores de columna eliminando caracteres invisibles 
    y comillas, preservando la capitalización original para coincidir con el DDL.

    Args:
        df (pl.DataFrame): DataFrame con encabezados originales.

    Returns:
        pl.DataFrame: DataFrame con identificadores sanitizados.
    """
    nuevas_columnas = [
        col.strip().replace("\n", "").replace('"', '').replace("'", "")
        for col in df.columns
    ]
    return df.rename(dict(zip(df.columns, nuevas_columnas)))


def aplicar_tipos_seguros(df: pl.DataFrame, reglas_tipos: Dict[str, Any]) -> pl.DataFrame:
    """
    Aplica coerciones de tipo tolerantes a fallos y limita la longitud de las 
    cadenas de texto basándose en los metadatos de la base de datos.

    Args:
        df (pl.DataFrame): Lote de datos normalizado.
        reglas_tipos (Dict[str, Any]): Diccionario maestro de mapeo de tipos.

    Returns:
        pl.DataFrame: DataFrame tipado y truncado a los límites del DDL.
    """
    if df.is_empty():
        return df

    df = estandarizar_nombres_columnas(df)
    expresiones = []

    for col in df.columns:
        col_up = col.upper()

        # 1. Aplicación de Safe Casting guiada por el diccionario maestro
        if col_up in reglas_tipos:
            dtype_destino = reglas_tipos[col_up]

            if dtype_destino == pl.Datetime:
                expr = (
                    pl.col(col)
                    .str.slice(0, 19)
                    .str.to_datetime(strict=False)
                    .alias(col)
                )
            elif dtype_destino == pl.Float64:
                expr = (
                    pl.col(col)
                    .str.replace_all(",", "")
                    .str.strip_chars()
                    .cast(pl.Float64, strict=False)
                    .alias(col)
                )
            else:
                expr = pl.col(col).cast(dtype_destino, strict=False).alias(col)

            expresiones.append(expr)

        # 2. Control de Longitud para columnas de texto restantes (Varchar)
        elif df.schema[col] == pl.Utf8:
            limite = LIMITES_LONGITUD.get(col_up, 1000)
            expr = pl.col(col).str.slice(0, limite).alias(col)
            expresiones.append(expr)

    return df.with_columns(expresiones) if expresiones else df