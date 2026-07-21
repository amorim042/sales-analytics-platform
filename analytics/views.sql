CREATE VIEW vw_sales_summary AS

SELECT
    f.sales,
    f.quantity,
    f.discount,
    f.profit,

    p.category,
    p.sub_category,

    l.country,
    l.region,
    l.state,
    l.city,

    s.ship_mode,

    c.segment

FROM fact_sales f

JOIN dim_product p
    ON f.product_id = p.id

JOIN dim_location l
    ON f.location_id = l.id

JOIN dim_shipping s
    ON f.shipping_id = s.id

JOIN dim_customer c
    ON f.customer_id = c.id;

CREATE VIEW vw_kpis AS

SELECT

    COUNT(*) AS total_orders,

    SUM(sales) AS total_sales,

    SUM(profit) AS total_profit,

    AVG(profit) AS average_profit,

    AVG(discount) AS average_discount,

    SUM(quantity) AS total_quantity

FROM fact_sales;

CREATE VIEW vw_sales_by_category AS

SELECT

    p.category,

    SUM(f.sales) AS total_sales,

    SUM(f.profit) AS total_profit,

    SUM(f.quantity) AS total_quantity

FROM fact_sales f

JOIN dim_product p
ON f.product_id = p.id

GROUP BY
p.category;