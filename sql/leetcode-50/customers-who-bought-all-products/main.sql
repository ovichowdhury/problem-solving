-- https://leetcode.com/problems/customers-who-bought-all-products/submissions/1816273498/?envType=study-plan-v2&envId=top-sql-50
WITH group_cust AS (
  SELECT
    customer_id,
    COUNT(DISTINCT product_key) AS product_count
  FROM customer
  GROUP BY customer_id
)
SELECT
  customer_id
FROM group_cust
WHERE product_count = (
  SELECT COUNT(*) FROM product
);