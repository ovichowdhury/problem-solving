-- https://leetcode.com/problems/product-price-at-a-given-date/?envType=study-plan-v2&envId=top-sql-50
WITH max_product AS (
  SELECT
    product_id,
    MAX(change_date) AS max_date
  FROM products
  WHERE change_date <= '2019-08-16'
  GROUP BY product_id
)
SELECT
  p.product_id,
  p.new_price AS price
FROM products AS p
INNER JOIN max_product AS m
  ON p.product_id = m.product_id
  AND p.change_date = m.max_date

UNION

SELECT
  product_id,
  10 AS price
FROM products
WHERE change_date > '2019-08-16'
GROUP BY product_id
HAVING product_id NOT IN (SELECT product_id FROM max_product)