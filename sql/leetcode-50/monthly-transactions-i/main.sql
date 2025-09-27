-- https://leetcode.com/problems/monthly-transactions-i/description/?envType=study-plan-v2&envId=top-sql-50

SELECT
  TO_CHAR(trans_date, 'YYYY-MM') AS month,
  country,
  COUNT(1) AS trans_count,
  COUNT(1) FILTER (WHERE state = 'approved') AS approved_count,
  SUM(amount) AS trans_total_amount,
  COALESCE(SUM(amount) FILTER (WHERE state = 'approved'), 0) AS approved_total_amount
FROM
  transactions
GROUP BY
  month,
  country;