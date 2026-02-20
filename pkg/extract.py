"""
extract.py

Módulo de ingesta de datos masivos mediante evaluación perezosa (Lazy Evaluation).
Utiliza el escáner nativo de Polars para crear un plan de ejecución optimizado,
delegando el manejo de codificación al motor subyacente en Rust y previniendo
desbordamientos de memoria (Out-of-Memory).
"""
from pathlib import Path
from typing import Iterator
import polars as pl


def get_sat_reader(file_path: Path, batch_size: int, separator: str = "|", skip_rows: int = 0) -> Iterator[pl.DataFrame]:
    """
    Inicializa un escáner de Polars para lectura fragmentada de archivos masivos.

    Args:
        file_path (Path): Ruta absoluta al archivo fuente.
        batch_size (int): Cantidad máxima de filas a procesar por lote en memoria.
        separator (str): Carácter delimitador utilizado en el archivo fuente.
        skip_rows (int): Filas a saltar utilizando Binary Seek (Bookmark).

    Returns:
        Iterator[pl.DataFrame]: Generador que entrega fragmentos (DataFrames) del archivo.

    Raises:
        FileNotFoundError: Si el archivo especificado no existe en la ruta.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"El archivo fuente no fue localizado: {file_path}")

    # RESOLUCIÓN DE LA TRAMPA DEL ENCABEZADO
    if skip_rows > 0:
        # 1. Leemos mágicamente solo la fila 0 para capturar los nombres de las columnas
        header_df = pl.read_csv(
            str(file_path), 
            separator=separator, 
            n_rows=0, 
            infer_schema_length=0, 
            quote_char=None,
            encoding="utf8-lossy",
            ignore_errors=True
        )
        nombres_columnas = header_df.columns
        
        # 2. Saltamos las filas + la fila física del encabezado, inyectando las columnas guardadas
        lazy_plan = pl.scan_csv(
            str(file_path),
            separator=separator,
            has_header=False, 
            skip_rows=skip_rows + 1, 
            new_columns=nombres_columnas,
            encoding="utf8-lossy",
            ignore_errors=True,
            truncate_ragged_lines=True,
            infer_schema_length=0,
            quote_char=None
        )
    else:
        # Flujo normal para el lote 1
        lazy_plan = pl.scan_csv(
            str(file_path),
            separator=separator,
            has_header=True,
            encoding="utf8-lossy",
            ignore_errors=True,
            truncate_ragged_lines=True,
            infer_schema_length=0,
            quote_char=None
        )
    
    # INYECCIÓN DEL NIVEL 1: Agregamos la FilaOrigen para salvar duplicados reales del SAT
    lazy_plan = lazy_plan.with_row_index("FilaOrigen", offset=skip_rows)
    
    # Ejecuta el plan fragmentándolo dinámicamente en lotes manejables
    return lazy_plan.collect_batches(chunk_size=batch_size)