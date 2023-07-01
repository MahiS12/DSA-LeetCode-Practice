# Write your MySQL query statement below

select e.unique_id, u.name
from Employees u left join EmployeeUNI e on e.id = u.id