"""
Módulo de perfilado estructural y volumétrico para esquemas de datos masivos (MODO LIGERO).

Provee herramientas analíticas para determinar la composición de columnas 
evadiendo el colapso de memoria (OOM) en archivos ultra-masivos (>100GB) 
alojados en unidades de red compartidas (SMB).
"""

import io
import sys
from typing import Any, Dict

import polars as pl

from pkg.globals import SAT_RAW_DIR


def profile_sat_table(nombre_archivo: str) -> None:
    """
    Ejecuta el escaneo de superficie mediante un bypass de red con Python nativo.
    """
    print("[INFO] INICIANDO PERFILADO FORENSE ESTRUCTURAL (MODO LIGERO BLINDADO)")
    print("=" * 135)

    # Resolución de ruta y validación de existencia
    ruta_completa = SAT_RAW_DIR / nombre_archivo
    
    if not ruta_completa.exists():
        print(f"[ERROR] Recurso no localizado en el directorio fuente: {ruta_completa}")
        sys.exit(1)

    print(f"\n[INFO] Analizando topología de: {nombre_archivo}...")
    print("[INFO] Aprovisionando lector en Modo Ligero (Bypass de Red) para protección de RAM...")

    try:
        # =========================================================================
        # [MODO LIGERO BLINDADO]: Bypass de red SMB usando Python puro.
        # Descargamos físicamente solo 50 líneas (Stream) y creamos un archivo 
        # virtual en RAM para que Polars NUNCA toque el archivo masivo.
        # =========================================================================
        lineas_muestra = []
        
        # Abrimos la tubería de red de forma segura y nativa
        with open(ruta_completa, "r", encoding="utf-8", errors="replace") as f:
            for _ in range(50):
                try:
                    lineas_muestra.append(next(f))
                except StopIteration:
                    break  # Si el archivo tiene menos de 50 líneas, nos detenemos
                    
        # Convertimos las 50 líneas en un archivo virtual en la memoria RAM (StringIO)
        archivo_virtual = io.StringIO("".join(lineas_muestra))

        # Ahora Polars lee el archivo virtual de ~10 KB, ignorando el disco de red
        df_batch = pl.read_csv(
            archivo_virtual,
            separator="|",
            infer_schema_length=0, 
            truncate_ragged_lines=True,
            ignore_errors=True,
            quote_char=None
        )

        # Normalización de representaciones vacías hacia nulos analíticos
        df_batch = df_batch.with_columns(pl.all().replace("", None))

        columnas = df_batch.columns
        total_filas_global = len(df_batch)
        nulos_por_columna = {c: df_batch[c].null_count() for c in columnas}
        
        ejemplos: Dict[str, Any] = {}
        for col in columnas:
            ejemplo_df = df_batch[col].drop_nulls().head(1)
            if len(ejemplo_df) > 0:
                ejemplos[col] = str(ejemplo_df.item())

        print("\n[INFO] Escaneo de superficie (Modo Ligero) finalizado exitosamente.")
        print(f"[RESULTADO] Muestra extraída: {total_filas_global:,} registros (Suficiente para Schema Drift).")
        print(f"[RESULTADO] Total de columnas detectadas: {len(columnas)}")
        
        # Renderizado del reporte tabular de topología
        print(f"\n{'No.':<4} | {'Nombre de Columna':<35} | {'% Nulos':<10} | {'Muestra de Dato'}")
        print("-" * 135)

        for i, col in enumerate(columnas):
            pct_nulos = (nulos_por_columna[col] / total_filas_global * 100) if total_filas_global > 0 else 0
            
            ejemplo_str = ejemplos.get(col, "NULL")
            # Truncamiento de muestra para mantener la integridad de la interfaz de consola
            ejemplo_final = (ejemplo_str[:50] + '...') if len(ejemplo_str) > 50 else ejemplo_str

            print(f"{(i + 1):<4} | {col:<35} | {pct_nulos:>8.2f}% | {ejemplo_final}")

        # =====================================================================
        # [NUEVA SECCIÓN]: Exportación rápida para cacería de Schema Drift
        # =====================================================================
        print("\n" + "-" * 135)
        print("[INFO] LISTA PLANA DE COLUMNAS (Ideal para copiar y comparar contra SQL/globals.py):")
        
        # Formatea las columnas como una lista de Python para fácil copiado
        lista_formateada = ",\n    ".join([f'"{c}"' for c in columnas])
        print(f"[\n    {lista_formateada}\n]")
        print("-" * 135)    

    except Exception as e:
        print(f"[CRITICAL ERROR] Fallo irrecuperable al procesar {nombre_archivo}: {e}")

    print("\n" + "=" * 135)


if __name__ == "__main__":
    # Análisis de argumentos por interfaz de línea de comandos (CLI)
    if len(sys.argv) < 2:
        print("[WARN] Uso de CLI incorrecto.")
        print("[INFO] Sintaxis esperada: python scripts_operativos/profile_sat_ligero.py <nombre_del_archivo.csv>")
        print("[INFO] Ejemplo: python scripts_operativos/profile_sat_ligero.py AECF_0101_Anexo4.csv.utf8")
    else:
        archivo_objetivo = sys.argv[1]
        profile_sat_table(archivo_objetivo)