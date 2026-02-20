"""
config.py
Gestión centralizada de credenciales y parámetros de conexión.
Depende estrictamente de las variables de entorno definidas en el archivo .env.
"""
import os
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

SERVER = os.getenv('DB_SERVER')
DATABASE = os.getenv('DB_NAME')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
DRIVER = os.getenv('DB_DRIVER', '{ODBC Driver 17 for SQL Server}')
TRUSTED = os.getenv('DB_TRUSTED', 'NO')


def get_connection_string() -> str:
    """
    Construye la cadena de conexión ODBC para SQLAlchemy.

    Returns:
        str: Cadena de conexión formateada.

    Raises:
        ValueError: Si faltan variables críticas de conexión en el entorno.
    """
    if not all([SERVER, DATABASE]):
        raise ValueError("Faltan variables críticas en el .env (DB_SERVER o DB_NAME).")

    if TRUSTED.upper() in ['YES', 'TRUE', '1']:
        auth_str = "Trusted_Connection=yes;"
    else:
        if not all([USER, PASSWORD]):
            raise ValueError("Faltan DB_USER o DB_PASSWORD en el .env para autenticación SQL.")
        auth_str = f"UID={USER};PWD={PASSWORD};"

    params = urllib.parse.quote_plus(
        f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};{auth_str}Encrypt=no;TrustServerCertificate=yes;"
    )
    return f"mssql+pyodbc:///?odbc_connect={params}"