-- https://leetcode.com/problems/consecutive-numbers/?envType=study-plan-v2&envId=top-sql-50
WITH lags AS (
  SELECT
    id,
    num,
    LAG(num, 1) OVER (ORDER BY id) AS prev_1,
    LAG(num, 2) OVER (ORDER BY id) AS prev_2
  FROM logs
)
SELECT DISTINCT
  num AS ConsecutiveNums
FROM lags
WHERE num = prev_1
  AND num = prev_2
  AND prev_1 = prev_2;