-- https://leetcode.com/problems/biggest-single-number/submissions/1816266117/?envType=study-plan-v2&envId=top-sql-50

SELECT COALESCE(
    (SELECT num
     FROM mynumbers
     GROUP BY num
     HAVING COUNT(*) = 1
     ORDER BY num DESC
     LIMIT 1),
    NULL
) AS num;