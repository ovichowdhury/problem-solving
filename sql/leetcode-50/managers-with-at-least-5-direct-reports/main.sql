-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/?envType=study-plan-v2&envId=top-sql-50
SELECT e1.name
FROM employee e1
INNER JOIN employee e2 ON e1.id = e2.managerId
GROUP BY e1.id, e1.name
HAVING COUNT(1) >= 5;
