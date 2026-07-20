CREATE TABLE dim_product (
    id SERIAL PRIMARY KEY,
    category VARCHAR(100),
    sub_category VARCHAR(100)
);

CREATE TABLE dim_location (
    id SERIAL PRIMARY KEY,
    country VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    region VARCHAR(50)
);

CREATE TABLE dim_customer (
    id SERIAL PRIMARY KEY,
    segment VARCHAR(50)
);

CREATE TABLE dim_shipping (
    id SERIAL PRIMARY KEY,
    ship_mode VARCHAR(50)
);

CREATE TABLE fact_sales (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL,
    location_id INTEGER NOT NULL,
    shipping_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    sales DECIMAL(10,2),
    quantity INTEGER,
    discount DECIMAL(5,2),
    profit DECIMAL(10,2),

    CONSTRAINT fk_product
        FOREIGN KEY(product_id)
        REFERENCES dim_product(id),

    CONSTRAINT fk_location
        FOREIGN KEY(location_id)
        REFERENCES dim_location(id),

    CONSTRAINT fk_shipping
        FOREIGN KEY(shipping_id)
        REFERENCES dim_shipping(id),

    CONSTRAINT fk_customer
        FOREIGN KEY(customer_id)
        REFERENCES dim_customer(id)
);