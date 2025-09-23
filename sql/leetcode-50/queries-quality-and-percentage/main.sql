-- https://leetcode.com/problems/queries-quality-and-percentage/?envType=study-plan-v2&envId=top-sql-50

SELECT 
  query_name,
  ROUND(
    SUM(rating::numeric / position) / COUNT(1),
    2
  ) AS quality,
  ROUND(
    (COUNT(*) FILTER (WHERE rating < 3)::numeric / COUNT(1)) * 100,
    2
  ) AS poor_query_percentage
FROM queries
GROUP BY query_name;