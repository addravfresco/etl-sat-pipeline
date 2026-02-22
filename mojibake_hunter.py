"""
mojibake_hunter.py (Versión Multi-Columna & Case-Insensitive)
Herramienta de perfilado de datos para aislar palabras corruptas (Mojibake).
Extrae palabras completas que contienen caracteres anómalos en múltiples columnas.
"""
import polars as pl
from pkg.cleaning_rules import REEMPLAZOS_MOJIBAKE 

# Configuración
ARCHIVO_SAT = r"\\sia\AECF\DGATIC\LOTA\Bases de Datos\SAT\GERG_AECF_1891_Anexo1A-QA.txt"

COLUMNAS_TEXTO = [
    "CondicionesDePago",
    "ReceptorNombre",
    "EmisorNombre" 
]

def cazar_mojibake():
    print(f"🔍 Iniciando escaneo forense multi-columna...")
    
    # 1. Extraemos las palabras conocidas y las forzamos a MAYÚSCULAS como escudo de seguridad
    palabras_conocidas = [palabra.upper() for palabra in REEMPLAZOS_MOJIBAKE.keys()]
    print(f"🛡️ Se ignorarán {len(palabras_conocidas)} palabras que ya están curadas en cleaning_rules.py")

    # Expresión regular: Busca palabras que contengan caracteres de corrupción conocidos
    regex_corrupcion = r"(?i)\b\w*[\ufffdÃÐÏ¿½¡]+\w*\b"

    lazy_df = pl.scan_csv(
        ARCHIVO_SAT,
        separator="|",
        encoding="utf8-lossy",
        ignore_errors=True,
        infer_schema_length=0
    )

    resultado = (
        lazy_df
        .select(COLUMNAS_TEXTO)
        .unpivot(on=COLUMNAS_TEXTO, value_name="TextoLibre")
        .drop_nulls("TextoLibre")
        .with_columns(
            pl.col("TextoLibre").str.extract_all(regex_corrupcion).alias("Palabras_Rotas")
        )
        .explode("Palabras_Rotas")
        .drop_nulls("Palabras_Rotas")
        
        # MAGIA DE NORMALIZACIÓN: Convertimos la palabra extraída a MAYÚSCULAS
        # Esto convierte "MUï¿½OZ" (minúscula corrupta) en "MUÏ¿½OZ" (mayúscula corrupta)
        .with_columns(
            pl.col("Palabras_Rotas").str.to_uppercase()
        )
        
        # MAGIA DE FILTRADO: Excluimos todo lo que ya existe en tu diccionario
        .filter(~pl.col("Palabras_Rotas").is_in(palabras_conocidas))
        
        .group_by("Palabras_Rotas")
        .agg(pl.len().alias("Frecuencia"))
        .sort("Frecuencia", descending=True)
    )

    print("⏳ Procesando (esto tomará unos minutos)...")
    df_final = resultado.collect(streaming=True)
    
    ruta_salida = "candidatos_mojibake_multicolumna.csv"
    df_final.write_csv(ruta_salida)
    
    print(f"✅ ¡Cacería terminada! Se encontraron {len(df_final)} palabras NUEVAS sospechosas.")
    print(f"📁 Revisa el archivo: {ruta_salida}")

if __name__ == "__main__":
    cazar_mojibake()