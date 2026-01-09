from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "1702"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "pizzaria_bi"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
