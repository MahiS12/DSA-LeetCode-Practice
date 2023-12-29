# Write your MySQL query statement below

# Select employee_id, department_id
# from Employee
# Where primary_flag = 'Y' or employee_id in (
#     Select employee_id
#     from Employee 
#     Group by employee_id
#     Having Count(employee_id) = 1 )

Select employee_id, department_id
from Employee
Where primary_flag = 'Y' 
UNION
Select employee_id,department_id
from Employee 
Group by employee_id
Having Count(employee_id) = 1 

