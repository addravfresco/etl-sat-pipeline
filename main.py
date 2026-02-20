"""
main.py
Orquestador Supremo del Pipeline ETL SAT (Optimizado).
Coordina el flujo de datos: Extracción (Lazy), Transformación (Vectorizada), 
Tipado (Enforcement) y Carga (Upsert Bulk).
"""
import os
import sys
import traceback

from pkg.globals import TABLES_CONFIG, REGLAS_DINAMICAS, SAT_RAW_DIR, BATCH_SIZE
from pkg.extract import get_sat_reader
from pkg.transform import transform_sat_batch
from pkg.enforcer import aplicar_tipos_seguros
from pkg.load import upload_to_sql_blindado
from pkg.reports import ETLReport
from pkg.checkpoint import leer_estado, guardar_estado  # <-- NUEVO MÓDULO IMPORTADO

# Configuración del entorno de salida para visualización de logs
try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(line_buffering=True)  # type: ignore
except AttributeError:
    pass


def main() -> None:
    # 1. Resolución de Identidad y Metadatos
    id_anexo = sys.argv[1].upper() if len(sys.argv) > 1 else "1A"

    if id_anexo not in TABLES_CONFIG:
        print(f"[ERROR] El Anexo '{id_anexo}' no está configurado en TABLES_CONFIG.")
        sys.exit(1)

    meta = TABLES_CONFIG[id_anexo]
    table_name = meta["table_name"]
    file_name = meta["file_name"]
    separator = meta["separator"]

    print(f"\n>>> INICIANDO SISTEMA ETL SAT: ANEXO {id_anexo} [OPTIMIZADO]")
    print(f">>> TABLA DESTINO: {table_name}")

    # 2. Validación de Disponibilidad de Recursos
    ruta_archivo = SAT_RAW_DIR / file_name
    if not ruta_archivo.exists():
        print(f"[ERROR] Recurso fuente no localizado: {ruta_archivo}")
        sys.exit(1)

    file_size_gb = os.path.getsize(ruta_archivo) / (1024**3)
    print(f"[INFO] Ingesta: {file_name} | Volumen: {file_size_gb:.2f} GB\n" + "-" * 60)

    # --- INICIO LÓGICA BOOKMARK ---
    filas_procesadas_historicas = leer_estado(id_anexo)
    if filas_procesadas_historicas > 0:
        print(f"[RECOVERY] Bookmark detectado. Retomando desde la fila: {filas_procesadas_historicas:,.0f}")
    else:
        print("[INFO] No hay Bookmark previo. Iniciando desde la fila 0.")
    # --- FIN LÓGICA BOOKMARK ---

    report = ETLReport()

    try:
        # 3. Inicialización del Stream de Lectura con Inyección de Coordenadas (skip_rows)
        reader = get_sat_reader(ruta_archivo, BATCH_SIZE, separator, skip_rows=filas_procesadas_historicas)
        print("[INFO] Plan de ejecución activo. Iniciando procesamiento en streaming...")

        # 4. Ciclo de Vida del Dato (Vectorizado)
        for df_batch in reader:
            # Guardamos la cantidad de filas físicas leídas del CSV antes de que las reglas de limpieza borren basura
            filas_leidas_en_este_lote = len(df_batch)
            
            # Fase B: Transformación y Saneamiento
            df_processed = transform_sat_batch(df_batch)
            
            # Fase C: Aplicación de Tipos y Control de Longitud
            df_final = aplicar_tipos_seguros(df_processed, REGLAS_DINAMICAS)
            
            # Fase D: Auditoría Forense
            report.audit_batch(df_final)
            
            # Fase E: Persistencia Masiva (Upsert)
            upload_to_sql_blindado(df_final, table_name, id_anexo)
            
            # Actualización de Telemetría
            report.update_metrics(len(df_final))
            
            # --- ACTUALIZACIÓN DEL BOOKMARK ---
            filas_procesadas_historicas += filas_leidas_en_este_lote
            guardar_estado(id_anexo, filas_procesadas_historicas)

        print("\n[INFO] Flujo finalizado exitosamente (EOF).")
        report_path = report.generate_final_report(id_anexo, file_name, status="SUCCESS")
        print(f"[INFO] Reporte de auditoría generado: {report_path}")

    except KeyboardInterrupt:
        print("\n[WARN] Operación cancelada por el operador.")
        report.generate_final_report(id_anexo, file_name, status="CANCELLED")
    except Exception as e:
        print(f"\n[CRITICAL ERROR] Fallo sistémico.")
        print(f"Detalle Técnico: {e}")
        print("-" * 60)
        traceback.print_exc()
        report.generate_final_report(id_anexo, file_name, status="FAILED", error_details=str(e))

if __name__ == "__main__":
    main()