-- https://leetcode.com/problems/confirmation-rate/?envType=study-plan-v2&envId=top-sql-50
WITH conf_rate AS (
    SELECT 
        s.user_id, 
        COUNT(c.action) AS total, 
        COUNT(*) FILTER (WHERE c.action = 'confirmed') AS confirmed
    FROM signups AS s 
    LEFT JOIN confirmations AS c
      ON s.user_id = c.user_id
    GROUP BY s.user_id
    ORDER BY s.user_id
)
SELECT 
    user_id,
    CASE 
        WHEN total = 0 THEN 0
        ELSE ROUND(confirmed::numeric / total, 2)
    END AS confirmation_rate
FROM conf_rate;
