"""
transform.py
Módulo vectorizado de saneamiento y normalización.
Ejecuta la limpieza masiva de Mojibake utilizando algoritmos de búsqueda 
simultánea en Rust, eliminando los cuellos de botella de Python.
"""
import polars as pl
from pkg.cleaning_rules import REEMPLAZOS_MOJIBAKE


def transform_sat_batch(df: pl.DataFrame) -> pl.DataFrame:
    """
    Ejecuta el pipeline de transformación vectorizada sobre un lote de datos.

    Fases:
        1. Normalización Global: Estandariza todas las columnas de texto (Utf8)
           eliminando espacios y forzando mayúsculas.
        2. Saneamiento Forense: Aplica el diccionario de Mojibake en columnas
           descriptivas utilizando 'replace_many' nativo de Polars.

    Args:
        df (pl.DataFrame): Lote de datos crudos.

    Returns:
        pl.DataFrame: DataFrame normalizado y saneado en memoria.
    """
    if df.is_empty():
        return df

    # Fase 1: Normalización de alto rendimiento nativa
    df = df.with_columns(
        pl.col(pl.Utf8).str.strip_chars().str.to_uppercase().name.keep()
    )

    # Fase 2: Identificación Automática de Columnas Sensibles
    palabras_clave = ["NOMBRE", "CONCEPTO", "DESCRIPCION"]
    
    cols_a_limpiar = [
        col for col in df.columns 
        if any(key in col.upper() for key in palabras_clave) and df.schema[col] == pl.Utf8
    ]

    # Fase 3: Limpieza Quirúrgica Vectorizada (Adiós a map_elements)
    if cols_a_limpiar:
        # Preparamos los patrones y reemplazos para el algoritmo Aho-Corasick
        patrones_sucios = list(REEMPLAZOS_MOJIBAKE.keys())
        valores_limpios = list(REEMPLAZOS_MOJIBAKE.values())

        df = df.with_columns(
            [
                pl.col(c)
                .str.replace_many(patrones_sucios, valores_limpios)
                .alias(c)
                for c in cols_a_limpiar
            ]
        )

    if "UUID" in df.columns:
        df = df.filter(
            pl.col("UUID").str.contains(r"^[A-Za-z0-9]{8}-[A-Za-z0-9]{4}-[A-Za-z0-9]{4}-[A-Za-z0-9]{4}-[A-Za-z0-9]{12}$")
        )    

    return df