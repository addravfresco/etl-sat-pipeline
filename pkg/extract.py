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


def get_sat_reader(file_path: Path, batch_size: int, separator: str = "|") -> Iterator[pl.DataFrame]:
    """
    Inicializa un escáner de Polars para lectura fragmentada de archivos masivos.

    Args:
        file_path (Path): Ruta absoluta al archivo fuente.
        batch_size (int): Cantidad máxima de filas a procesar por lote en memoria.
        separator (str): Carácter delimitador utilizado en el archivo fuente.

    Returns:
        Iterator[pl.DataFrame]: Generador que entrega fragmentos (DataFrames) del archivo.

    Raises:
        FileNotFoundError: Si el archivo especificado no existe en la ruta.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"El archivo fuente no fue localizado: {file_path}")

    # Generación del plan de ejecución perezoso (No carga datos a la memoria RAM)
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
    
    # Ejecuta el plan fragmentándolo dinámicamente en lotes manejables
    return lazy_plan.collect_batches(chunk_size=batch_size)