import pandas as pd
import os
from db_config import engine

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")

# Ler CSVs

df_pizza = pd.read_csv(os.path.join(RAW_DIR, "dim_pizza.csv"))
df_data = pd.read_csv(os.path.join(RAW_DIR, "dim_data.csv"))
df_pedidos = pd.read_csv(os.path.join(RAW_DIR, "fact_pedidos.csv"))

# Ajustes simples ETL

df_data["data"] = pd.to_datetime(df_data["data"], format="%Y-%m-%d")

# horario vem como texto "HH:MM:SS"
df_pedidos["horario"] = pd.to_datetime(df_pedidos["horario"], format="%H:%M:%S").dt.time

# pedidos veio com 2 colunas que são df
df_pedidos = df_pedidos.drop(columns=["data", "pizza"])

# Evitar duplicar carga (se você rodar mais de 1 vez)

with engine.begin() as conn:
    conn.exec_driver_sql("TRUNCATE TABLE fact_pedidos, dim_pizza, dim_data RESTART IDENTITY CASCADE;")

# Carregar no PostgreSQL

df_pizza.to_sql("dim_pizza", engine, if_exists="append", index=False)
df_data.to_sql("dim_data", engine, if_exists="append", index=False)
df_pedidos.to_sql("fact_pedidos", engine, if_exists="append", index=False)

print("Dados carregados no PostgreSQL com sucesso!")
