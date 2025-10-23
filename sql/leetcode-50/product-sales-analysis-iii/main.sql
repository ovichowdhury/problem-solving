-- https://leetcode.com/problems/product-sales-analysis-iii/?envType=study-plan-v2&envId=top-sql-50
SELECT
  s.product_id,
  s.year       AS first_year,
  s.quantity,
  s.price
FROM sales AS s
INNER JOIN (
  SELECT DISTINCT ON (product_id)
    product_id,
    year AS first_year
  FROM sales
  ORDER BY product_id, year ASC
) AS f
ON s.product_id = f.product_id
AND s.year = f.first_year;
