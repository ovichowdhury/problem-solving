
-- https://leetcode.com/problems/movie-rating/?envType=study-plan-v2&envId=top-sql-50
SELECT name AS results
FROM (
    SELECT u.name, COUNT(*) AS cnt
    FROM movies AS m
        INNER JOIN movierating AS mr ON m.movie_id = mr.movie_id
        INNER JOIN users AS u ON u.user_id = mr.user_id
    GROUP BY u.name
    ORDER BY cnt DESC, u.name ASC
    LIMIT 1
)

UNION ALL

SELECT title AS results
FROM (
    SELECT m.title, AVG(mr.rating) AS average
    FROM movies AS m
        INNER JOIN movierating AS mr ON m.movie_id = mr.movie_id
    WHERE TO_CHAR(created_at, 'YYYY-MM') = '2020-02'
    GROUP BY m.title
    ORDER BY average DESC, m.title ASC
    LIMIT 1
)