import pandas as pd
import random
import os
from faker import Faker
from datetime import datetime, timedelta, time

fake = Faker("pt_BR")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
os.makedirs(RAW_DIR, exist_ok=True)

# Pizza (catálogo)

pizzas = [
    ("Margherita", "Tradicional", 39.90),
    ("Calabresa", "Tradicional", 42.90),
    ("Mussarela", "Tradicional", 41.90),
    ("Portuguesa", "Tradicional", 46.90),
    ("Frango com Catupiry", "Especial", 49.90),
    ("Quatro Queijos", "Especial", 48.90),
    ("Pepperoni", "Especial", 52.90),
    ("Vegetariana", "Leve", 47.90),
    ("Chocolate", "Doce", 44.90),
    ("Banana com Canela", "Doce", 43.90),
]

df_pizzas = pd.DataFrame([
    {"pizza_id": i + 1, "pizza": p[0], "categoria": p[1], "preco": p[2]}
    for i, p in enumerate(pizzas)
])

# Data (calendário)

datas = []
data_inicio = datetime(2024, 1, 1)
data_fim = datetime(2024, 3, 31)  # 3 meses para ficar leve e rápido para testes simples

current_date = data_inicio
date_id = 1

while current_date <= data_fim:
    datas.append({
        "date_id": date_id,
        "data": current_date.date(),
        "ano": current_date.year,
        "mes": current_date.month,
        "dia": current_date.day,
        "dia_semana": current_date.strftime("%A")
    })
    current_date += timedelta(days=1)
    date_id += 1

df_datas = pd.DataFrame(datas)


# Pedidos: ID, data, horário, endereço, pizza

def gerar_horario_pedido() -> str:
    hora = random.randint(18, 23)
    minuto = random.choice([0, 10, 15, 20, 30, 40, 45, 50])
    return f"{hora:02d}:{minuto:02d}:00"

pedidos = []
N_PEDIDOS = 4000

for pedido_id in range(1, N_PEDIDOS + 1):
    d = df_datas.sample(1).iloc[0]
    pizza = df_pizzas.sample(1).iloc[0]

    quantidade = random.randint(1, 3)
    valor_total = round(float(pizza["preco"]) * quantidade, 2)

    pedidos.append({
        "pedido_id": pedido_id,
        "date_id": int(d["date_id"]),
        "data": str(d["data"]),
        "horario": gerar_horario_pedido(),
        "endereco": fake.address().replace("\n", ", "),
        "pizza_id": int(pizza["pizza_id"]),
        "pizza": str(pizza["pizza"]),
        "quantidade": quantidade,
        "valor_total": valor_total
    })

df_pedidos = pd.DataFrame(pedidos)

# Salvar CSVs (raw)

df_pizzas.to_csv(os.path.join(RAW_DIR, "dim_pizza.csv"), index=False)
df_datas.to_csv(os.path.join(RAW_DIR, "dim_data.csv"), index=False)
df_pedidos.to_csv(os.path.join(RAW_DIR, "fact_pedidos.csv"), index=False)

print("Dados brutos da pizzaria gerados em data/raw/")
print("Arquivos: dim_pizza.csv, dim_data.csv, fact_pedidos.csv")
