# analyzer/exporter.py
import pandas as pd
import sqlite3

def export_to_csv(df, filename="output.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"[+] Exported to CSV: {filename}")
    except Exception as e:
        print(f"[!] Failed to export to CSV: {e}")

def export_to_sqlite(df, db="logs.db", table="anomalies"):
    try:
        conn = sqlite3.connect(db)
        df.to_sql(table, conn, if_exists="replace", index=False)
        conn.close()
        print(f"[+] Exported to SQLite DB: {db}, Table: {table}")
    except Exception as e:
        print(f"[!] Failed to export to SQLite: {e}")
