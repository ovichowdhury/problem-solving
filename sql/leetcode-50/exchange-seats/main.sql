-- https://leetcode.com/problems/exchange-seats/?envType=study-plan-v2&envId=top-sql-50
SELECT
    id,
    CASE
        WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM seat)
            THEN student
        WHEN id % 2 = 1
            THEN LEAD(student) OVER (ORDER BY id)
        ELSE
            LAG(student) OVER (ORDER BY id)
    END AS student
FROM seat
ORDER BY id;
