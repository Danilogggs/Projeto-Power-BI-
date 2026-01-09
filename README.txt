Projeto BI – Pizzaria (PostgreSQL, Python e Power BI)

Este é um projeto didático de Business Intelligence, criado com o objetivo de praticar, na prática, todo o fluxo de dados usado em projetos reais de BI.

O cenário escolhido foi o de uma pizzaria, onde os pedidos são gerados, tratados, armazenados em banco de dados e analisados por meio de visualizações no Power BI.

Objetivo do projeto

O objetivo principal foi construir um pipeline completo de dados, passando pelas seguintes etapas:

- Geração de dados simulados de pedidos de uma pizzaria
- Tratamento e preparação dos dados com Python
- Armazenamento dos dados em um banco PostgreSQL
- Criação de consultas e views SQL para análise
- Visualização dos resultados no Power BI

O foco do projeto é aprendizado e consolidação de conceitos de BI, SQL e análise de dados.

Tecnologias utilizadas

- Python
- pandas
- faker
- sqlalchemy
- PostgreSQL
- Power BI Desktop

Estrutura do projeto
data/
 ├── raw/          # Dados brutos gerados pelo script Python
 └── processed/    # (reservado para dados tratados)

python/
 ├── 01_generate_data.py   # Geração dos dados da pizzaria
 ├── 02_etl_clean.py       # ETL e carregamento no PostgreSQL
 └── db_config.py          # Configuração de conexão com o banco

sql/
 ├── 01_create_tables.sql  # Criação das tabelas
 └── 02_views.sql          # Views 

powerbi/
 └── pizzaria_dashboard.pbix


Com os dados carregados e tratados, o projeto permite analisar, por exemplo:

- Receita diária da pizzaria
- Pizzas mais vendidas
- Horários de pico de pedidos
- Volume total de vendas no período
- Essas análises são apresentadas em um dashboard no Power BI.

Observações

Os dados utilizados são simulados, gerados por script, e não representam dados reais.
O projeto foi desenvolvido com foco em aprendizado e portfólio.
