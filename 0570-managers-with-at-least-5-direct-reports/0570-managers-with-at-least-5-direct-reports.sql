# Write your MySQL query statement below

select e.name
from Employee e
join Employee m
on e.id = m.managerid
Group by m.managerid
HAVING COUNT(*) >= 5
