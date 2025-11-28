-- https://leetcode.com/problems/last-person-to-fit-in-the-bus/?envType=study-plan-v2&envId=top-sql-50

WITH cqueue AS (
    SELECT
        turn,
        person_id,
        person_name,
        weight,
        SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM queue
)
SELECT
    person_name
FROM
    cqueue
WHERE
    cumulative_weight <= 1000
ORDER BY
    turn DESC
LIMIT 1;