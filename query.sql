DROP TABLE IF EXISTS final_output;

CREATE TABLE final_output AS
SELECT
    u.first_name || ' ' || u.last_name AS user_name,
    p.name AS product_title,
    o.order_date,
    oi.quantity,
    oi.unit_price AS price,
    pay.amount AS amount_paid,
    pay.payment_method
FROM orders AS o
JOIN users AS u ON u.user_id = o.user_id
JOIN order_item AS oi ON oi.order_id = o.order_id
JOIN product AS p ON p.product_id = oi.product_id
LEFT JOIN payments AS pay ON pay.order_id = o.order_id
ORDER BY o.order_date ASC, o.order_id, oi.order_item_id;

