import json
from pathlib import Path

# Definimos el nombre del archivo minúsculo que servirá de marcapáginas
ESTADO_FILE = "estado_etl.json"

def leer_estado(anexo_id: str) -> int:
    """
    Lee el archivo JSON para saber en qué fila se quedó un anexo específico.
    Si el archivo no existe o es la primera vez que se corre, devuelve 0.
    """
    ruta_archivo = Path(ESTADO_FILE)
    
    if ruta_archivo.exists():
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            try:
                datos = json.load(f)
                # Buscamos el estado específico del anexo (ej. "2B" o "1A")
                return datos.get(anexo_id, 0)
            except json.JSONDecodeError:
                # Si el archivo se corrompió por un apagón justo al guardar, empezamos de 0
                return 0
    return 0

def guardar_estado(anexo_id: str, filas_procesadas: int) -> None:
    """
    Actualiza el archivo JSON con el nuevo total de filas procesadas para un anexo.
    """
    ruta_archivo = Path(ESTADO_FILE)
    datos = {}
    
    # Si el archivo ya existe, cargamos lo que tiene para no borrar el estado de otros anexos
    if ruta_archivo.exists():
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            try:
                datos = json.load(f)
            except json.JSONDecodeError:
                pass # Si está corrupto, lo sobreescribiremos
                
    # Actualizamos solo el anexo que se está procesando en este momento
    datos[anexo_id] = filas_procesadas
    
    # Guardamos el archivo
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)