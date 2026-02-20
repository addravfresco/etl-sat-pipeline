"""
reports.py
Sistema de Telemetría, Auditoría y Control de Calidad.
Supervisa el rendimiento y detecta degradación en la calidad de los datos.
"""
import time
from datetime import datetime
from pathlib import Path
from typing import Set

import polars as pl
from pkg.globals import LOG_DIR

class ETLReport:
    """Controlador de telemetría y auditoría dinámica para procesos ETL."""

    def __init__(self):
        self.start_time = time.time()
        self.total_rows = 0
        self.total_batches = 0
        self.alerts_mojibake = 0
        self.alerts_length = 0
        self.alerts_nulls = 0
        self.samples_mojibake: Set[str] = set()
        self.samples_length: Set[str] = set()

        # Patrón heurístico para identificar fallos de codificación
        self.regex_mojibake = r"[?ÃÂƒ†‡‰‹›ŒŽ‘’“”•–—˜™š›œžŸ¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿Ðð]"
        self.min_text_length = 3

    def audit_batch(self, df: pl.DataFrame) -> None:
        """Ejecuta una auditoría selectiva sobre columnas descriptivas del lote."""
        keywords = ["NOMBRE", "CONCEPTO", "DESCRIPCION"]

        cols_audit = [
            c for c in df.columns
            if any(k in c.upper() for k in keywords) and df.schema[c] == pl.Utf8
        ]

        if not cols_audit:
            return

        for col in cols_audit:
            # 1. Monitoreo de Nulos
            n_nulls = df.filter(pl.col(col).is_null()).height
            if n_nulls > 0:
                self.alerts_nulls += n_nulls

            df_valid = df.filter(pl.col(col).is_not_null())
            if df_valid.height == 0:
                continue

            # 2. Análisis de Mojibake
            suspect_mojibake = df_valid.filter(pl.col(col).str.contains(self.regex_mojibake))
            if suspect_mojibake.height > 0:
                self.alerts_mojibake += suspect_mojibake.height
                samples = suspect_mojibake.select(col).unique().head(5).to_series().to_list()
                self.samples_mojibake.update([f"[{col}] {s}" for s in samples])

            # 3. Análisis de Mutilación
            suspect_len = df_valid.filter(pl.col(col).str.len_chars() < self.min_text_length)
            if suspect_len.height > 0:
                self.alerts_length += suspect_len.height
                samples = suspect_len.select(col).unique().head(3).to_series().to_list()
                self.samples_length.update([f"[{col}] {s}" for s in samples])

    def update_metrics(self, rows_count: int) -> None:
        """Actualiza los contadores globales y reporta velocidad."""
        self.total_rows += rows_count
        self.total_batches += 1
        elapsed = time.time() - self.start_time
        speed = self.total_rows / (elapsed + 1e-6)
        print(f"[INFO] Lote {self.total_batches:04d} | Filas Totales: {self.total_rows:,.0f} | Vel: {speed:,.0f} regs/seg")

    def generate_final_report(self, id_anexo: str, file_name: str, status: str = "SUCCESS", error_details: str = "") -> Path:
        """Genera el artefacto final de auditoría en disco."""
        total_duration = (time.time() - self.start_time) / 60
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"AUDIT_{id_anexo}_{timestamp}.txt"
        report_path = LOG_DIR / log_filename

        lines = [
            "=" * 80,
            f"DOCUMENTO AUDITADO: {file_name}",
            "=" * 80,
            f"SAT ETL AUDIT REPORT - ANEXO {id_anexo}",
            "-" * 80,
            f"Execution Status: {status}",
            f"Total Duration:   {total_duration:.2f} minutes",
            f"Processed Rows:   {self.total_rows:,.0f}",
            "-" * 80,
            "QUALITY SUMMARY",
            "-" * 80,
            f"Encoding Alerts (Mojibake): {self.alerts_mojibake}",
            f"Integrity Alerts (Nulls):    {self.alerts_nulls}",
            f"Mutilation Alerts (Short):   {self.alerts_length}",
            "=" * 80,
        ]

        if self.samples_mojibake:
            lines.append("\n[EVIDENCE] MOJIBAKE SAMPLES DETECTED:")
            lines.extend([f"  > {s}" for s in sorted(list(self.samples_mojibake))[:50]])

        if error_details:
            lines.append(f"\n[CRITICAL ERROR DETAILS]\n{error_details}")

        try:
            with open(report_path, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            return report_path
        except Exception as e:
            print(f"[ERROR] No se pudo escribir el reporte: {e}")
            return Path("ERROR")