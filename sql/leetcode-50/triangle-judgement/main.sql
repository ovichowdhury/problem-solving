-- https://leetcode.com/problems/triangle-judgement/?envType=study-plan-v2&envId=top-sql-50
SELECT
  x,
  y,
  z,
  CASE
    WHEN ABS(x + y) > ABS(z)
      AND ABS(x + z) > ABS(y)
      AND ABS(z + y) > ABS(x) THEN 'Yes'
    ELSE 'No'
  END AS triangle
FROM triangle;
