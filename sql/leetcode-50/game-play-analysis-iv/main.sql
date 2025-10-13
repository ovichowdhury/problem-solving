-- https://leetcode.com/problems/game-play-analysis-iv/?envType=study-plan-v2&envId=top-sql-50
WITH first_login AS (
    SELECT 
        player_id,
        MIN(event_date) AS first_date
    FROM activity
    GROUP BY player_id
),
next_day_login AS (
    SELECT 
        f.player_id
    FROM first_login f
    JOIN activity a
      ON a.player_id = f.player_id
     AND a.event_date = f.first_date + INTERVAL '1 day'
)
SELECT 
    ROUND(
        (SELECT COUNT(DISTINCT player_id) FROM next_day_login)::NUMERIC
        /
        (SELECT COUNT(DISTINCT player_id) FROM activity),
        2
    ) AS fraction;




