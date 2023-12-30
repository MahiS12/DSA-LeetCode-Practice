# Write your MySQL query statement below


Select t.name as results
from (SELECT u.name, COUNT(m.user_id) AS rating_count
FROM MovieRating m
JOIN Users u ON u.user_id = m.user_id
GROUP BY u.name
ORDER BY rating_count DESC, u.name ASC
LIMIT 1) as t

Union all

select new.title as results
from (
    Select m2.title, AVG(m1.rating) as av
    from MovieRating m1
    join Movies m2 on m2.movie_id = m1.movie_id
    where Month(m1.created_at) = 2 and Year(m1.created_at) = 2020
    Group by m2.title
    order by av DESC, m2.title ASC
    Limit 1
) as new


# (
# SELECT u.name AS results
# FROM Users u
# LEFT JOIN MovieRating m ON u.user_id = m.user_id
# GROUP BY u.name
# ORDER BY COUNT(m.user_id) DESC, u.name
# LIMIT 1
# )
# UNION ALL
# (
# SELECT m.title AS results
# FROM Movies m
# LEFT JOIN MovieRating mr ON m.movie_id = mr.movie_id
# WHERE mr.created_at like "2020-02-%"
# GROUP BY mr.movie_id
# ORDER BY AVG(mr.rating) DESC, m.title
# LIMIT 1
# )




