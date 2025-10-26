import sqlite3
import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Ruta donde se guardará el archivo CSV
ruta_guardado = r"C:\Users\ANYELO\Documents\PRUEBA TECNICA - ANALISTA DE DATOS\4. TABLEAU"

# Crear la carpeta si no existe
os.makedirs(ruta_guardado, exist_ok=True)

# Crear conexión SQLite temporal
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Crear tabla ventas_ciudades
cursor.execute("""
CREATE TABLE IF NOT EXISTS ventas_ciudades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ciudad TEXT,
    fecha DATE,
    monto_venta DECIMAL(10,2)
)
""")

# Lista de ciudades colombianas
ciudades = [
    "Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena",
    "Bucaramanga", "Pereira", "Manizales", "Santa Marta", "Cúcuta"
]

# Generar datos del último año
inicio = datetime(2024, 11, 1)
data = []
for i in range(365):
    fecha = inicio + timedelta(days=i)
    for ciudad in ciudades:
        monto = random.randint(5_000_000, 50_000_000)  # monto entre 5M y 50M
        data.append((ciudad, fecha.strftime("%Y-%m-%d"), monto))

# Insertar datos
cursor.executemany("INSERT INTO ventas_ciudades (ciudad, fecha, monto_venta) VALUES (?, ?, ?)", data)
conn.commit()

# Exportar a CSV
df = pd.read_sql("SELECT * FROM ventas_ciudades", conn)

ruta_archivo = os.path.join(ruta_guardado, "ventas_ciudades.csv")
df.to_csv(ruta_archivo, index=False, encoding="utf-8-sig")

conn.close()

print(f"✅ Dataset 'ventas_ciudades.csv' creado correctamente en:\n{ruta_archivo}")
print("\nColumnas del dataset:")
print(df.columns.tolist())
print("\nEjemplo de datos:")
print(df.head())
