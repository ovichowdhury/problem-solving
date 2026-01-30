-- https://leetcode.com/problems/restaurant-growth/?envType=study-plan-v2&envId=top-sql-50

WITH daily AS (
    SELECT
        visited_on,
        SUM(amount) AS daily_amount
    FROM customer
    GROUP BY visited_on
)
SELECT
    d1.visited_on,
    (
        SELECT SUM(daily_amount)
        FROM daily AS d2
        WHERE d2.visited_on BETWEEN d1.visited_on - INTERVAL '6 days' AND d1.visited_on
    ) AS amount,
    ROUND(
        (
            SELECT AVG(daily_amount)
            FROM daily AS d2
            WHERE d2.visited_on BETWEEN d1.visited_on - INTERVAL '6 days' AND d1.visited_on
        ),
        2
    ) AS average_amount
FROM daily AS d1
WHERE (
    SELECT COUNT(*)
    FROM daily AS d2
    WHERE d2.visited_on BETWEEN d1.visited_on - INTERVAL '6 days' AND d1.visited_on
) = 7
ORDER BY d1.visited_on ASC;
    where

