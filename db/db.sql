CREATE TABLE daily_sales (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_id VARCHAR(10),
    product VARCHAR(50),
    quantity INT,
    price NUMERIC,
    total_amount NUMERIC
);