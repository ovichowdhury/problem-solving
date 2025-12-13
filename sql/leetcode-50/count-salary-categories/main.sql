-- https://leetcode.com/problems/count-salary-categories/?envType=study-plan-v2&envId=top-sql-50
WITH low_sal AS (
  SELECT 'Low Salary' AS category, COUNT(1) AS accounts_count
  FROM accounts
  WHERE income < 20000
),
avg_sal AS (
  SELECT 'Average Salary' AS category, COUNT(1) AS accounts_count
  FROM accounts
  WHERE income BETWEEN 20000 AND 50000
),
high_sal AS (
  SELECT 'High Salary' AS category, COUNT(1) AS accounts_count
  FROM accounts
  WHERE income > 50000
)
SELECT * FROM low_sal
UNION
SELECT * FROM avg_sal
UNION
SELECT * FROM high_sal
