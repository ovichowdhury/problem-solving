-- https://leetcode.com/problems/primary-department-for-each-employee/?envType=study-plan-v2&envId=top-sql-50
SELECT
  employee_id,
  department_id
FROM
  employee
WHERE
  primary_flag = 'Y'
UNION
SELECT
  employee_id,
  MIN(department_id) AS department_id
FROM
  employee
GROUP BY
  employee_id
HAVING
  COUNT(department_id) = 1;