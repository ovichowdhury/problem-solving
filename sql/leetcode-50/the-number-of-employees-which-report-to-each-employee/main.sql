-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/?envType=study-plan-v2&envId=top-sql-50
SELECT
  e1.employee_id AS employee_id,
  e1.name AS name,
  COUNT(e2.employee_id) AS reports_count,
  ROUND(AVG(e2.age)) AS average_age
FROM employees e1
INNER JOIN employees e2
  ON e1.employee_id = e2.reports_to
GROUP BY
  e1.employee_id,
  e1.name
ORDER BY
  e1.employee_id ASC;