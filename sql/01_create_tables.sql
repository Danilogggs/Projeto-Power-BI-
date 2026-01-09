
-- Pizza

CREATE TABLE dim_pizza (
    pizza_id INTEGER PRIMARY KEY,
    pizza VARCHAR(100),
    categoria VARCHAR(50),
    preco NUMERIC(10,2)
);

-- Data

CREATE TABLE dim_data (
    date_id INTEGER PRIMARY KEY,
    data DATE,
    ano INTEGER,
    mes INTEGER,
    dia INTEGER,
    dia_semana VARCHAR(20)
);


-- Pedidos

CREATE TABLE fact_pedidos (
    pedido_id INTEGER PRIMARY KEY,
    date_id INTEGER,
    horario TIME,
    endereco TEXT,
    pizza_id INTEGER,
    quantidade INTEGER,
    valor_total NUMERIC(10,2),

    CONSTRAINT fk_data
        FOREIGN KEY (date_id) REFERENCES dim_data (date_id),

    CONSTRAINT fk_pizza
        FOREIGN KEY (pizza_id) REFERENCES dim_pizza (pizza_id)
);
