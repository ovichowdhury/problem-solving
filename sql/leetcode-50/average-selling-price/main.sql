-- Write your PostgreSQL query statement below
-- Calculate the average price per product, weighted by units sold
WITH slab AS (
    SELECT
        p.product_id,
        u.purchase_date,
        COALESCE(SUM(p.price * u.units), 0) AS slab_price,
        COALESCE(u.units, 0) AS units
    FROM prices AS p
    LEFT JOIN unitssold AS u
        ON p.product_id = u.product_id
        AND u.purchase_date BETWEEN p.start_date AND p.end_date
    GROUP BY
        p.product_id,
        u.purchase_date,
        u.units
)
SELECT
    product_id,
    COALESCE(
        ROUND(SUM(slab_price) / NULLIF(SUM(units), 0), 2), 
        0
    ) AS average_price
FROM slab
GROUP BY product_id;

