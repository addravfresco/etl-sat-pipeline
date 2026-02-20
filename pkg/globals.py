"""
globals.py
Configuración del entorno de ejecución, rutas maestras y reglas de negocio globales.
Gestiona la infraestructura de memoria para procesamiento Out-of-Core en Polars.
"""
import os
from pathlib import Path
import polars as pl

# --- 1. RUTAS E INFRAESTRUCTURA ---
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
TEMP_DIR = BASE_DIR / "temp_processing"
SAT_RAW_DIR = Path(r"\\sia\AECF\DGATIC\LOTA\Bases de Datos\SAT")

for folder in [LOG_DIR, TEMP_DIR]:
    folder.mkdir(parents=True, exist_ok=True)

# --- 2. GESTIÓN DE MEMORIA Y RENDIMIENTO ---
# Redireccionamiento crítico para evitar desbordamiento de RAM en la unidad C:
DISCO_TRABAJO = Path(r"D:\SAT\ETL_TEMP")
DISCO_TRABAJO.mkdir(parents=True, exist_ok=True)

os.environ["POLARS_TEMP_DIR"] = str(DISCO_TRABAJO)
os.environ["TMPDIR"] = str(DISCO_TRABAJO)
os.environ["TEMP"] = str(DISCO_TRABAJO)
os.environ["TMP"] = str(DISCO_TRABAJO)

# Limitación de concurrencia para evitar bloqueos por CPU
os.environ["POLARS_MAX_THREADS"] = "4"
pl.Config.set_tbl_rows(20)
pl.Config.set_fmt_str_lengths(50)

BATCH_SIZE = 100_000

# --- 3. DICCIONARIO MAESTRO DE TABLAS ---
TABLES_CONFIG = {
    "1A": {
        "file_name": "GERG_AECF_1891_Anexo1A-QA.txt",
        "table_name": "ANEXO_1A_2025_1S",
        "separator": "|"
    },
    "2B": {
        "file_name": "GERG_AECF_1891_Anexo2B.csv",
        "table_name": "ANEXO_2B_2025_1S",
        "separator": "|"
    }
}

# --- 4. REGLAS DE TIPADO DINÁMICO ---
# Catálogo estricto de tipos para enforcement previo a la base de datos.
REGLAS_DINAMICAS = {
    "UUID": pl.Utf8,
    "EMISORRFC": pl.Utf8,
    "RECEPTORRFC": pl.Utf8,
    "FECHAEMISION": pl.Datetime,
    "FECHACERTIFICACION": pl.Datetime,
    "FECHACANCELACION": pl.Datetime,
    "DESCUENTO": pl.Float64,
    "SUBTOTAL": pl.Float64,
    "TOTAL": pl.Float64,
    "TRASLADOSIVA": pl.Float64,
    "TRASLADOSIEPS": pl.Float64,
    "TOTALIMPUESTOSTRASLADADOS": pl.Float64,
    "RETENIDOSIVA": pl.Float64,
    "RETENIDOSISR": pl.Float64,
    "TOTALIMPUESTOSRETENIDOS": pl.Float64,
    "TIPOCAMBIO": pl.Float64,
    "CONCEPTOCANTIDAD": pl.Float64,
    "CONCEPTOVALORUNITARIO": pl.Float64,
    "CONCEPTOIMPORTE": pl.Float64,
}