import time
from pathlib import Path

def contar_lineas_rapido(ruta_archivo):
    print(f"Iniciando conteo forense de: {ruta_archivo}")
    print("Por favor espera, leyendo directamente del disco...")
    
    start_time = time.time()
    contador = 0
    
    try:
        with open(ruta_archivo, 'rb') as f:
            for _ in f:
                contador += 1
    except FileNotFoundError:
        print("¡Archivo no encontrado! Revisa la ruta.")
        return

    end_time = time.time()
    minutos = (end_time - start_time) / 60
    
    print(f"✅ ¡Conteo finalizado!")
    print(f"📊 Total de filas: {contador:,.0f}")
    print(f"⏱️ Tiempo que tomó: {minutos:.2f} minutos\n")


ruta_csv = r"\\sia\AECF\DGATIC\LOTA\Bases de Datos\SAT\GERG_AECF_1891_Anexo2B.csv"
ruta_txt_qa = r"\\sia\AECF\DGATIC\LOTA\Bases de Datos\SAT\GERG_AECF_1891_Anexo2B-QA.txt" 

#contar_lineas_rapido(ruta_csv)
contar_lineas_rapido(ruta_txt_qa) 