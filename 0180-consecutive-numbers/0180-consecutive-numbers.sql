# Write your MySQL query statement below


Select distinct(num) as ConsecutiveNums
from Logs
Where (id+1,num) in (select* from Logs) and (id+2, num) in (select* from Logs) 