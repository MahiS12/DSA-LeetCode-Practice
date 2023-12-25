# Write your MySQL query statement below

# SELECT e.name
# FROM Employee e
# JOIN Employee m ON e.id = m.managerId
# GROUP BY e.id
# HAVING COUNT(*) >= 5;

select name
from Employee
where id in (
    Select managerid
    from Employee
    Group by managerid
    Having count(*) >=5
)
