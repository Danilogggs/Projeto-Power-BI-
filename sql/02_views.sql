-- Receita total por dia

CREATE OR REPLACE VIEW vw_receita_por_dia AS
SELECT
    d.data,
    SUM(f.valor_total) AS receita_total
FROM fact_pedidos f
JOIN dim_data d ON f.date_id = d.date_id
GROUP BY d.data
ORDER BY d.data;

-- Pizzas mais vendidas

CREATE OR REPLACE VIEW vw_pizzas_mais_vendidas AS
SELECT
    p.pizza,
    SUM(f.quantidade) AS total_vendida,
    SUM(f.valor_total) AS receita_total
FROM fact_pedidos f
JOIN dim_pizza p ON f.pizza_id = p.pizza_id
GROUP BY p.pizza
ORDER BY total_vendida DESC;

-- Horários de maior fluxo

CREATE OR REPLACE VIEW vw_horarios_pico AS
SELECT
    EXTRACT(HOUR FROM f.horario) AS hora,
    COUNT(*) AS total_pedidos,
    SUM(f.valor_total) AS receita_total
FROM fact_pedidos f
GROUP BY hora
ORDER BY total_pedidos DESC;
