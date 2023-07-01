# Write your MySQL query statement below

select t1.machine_id, ROUND(AVG(t2.timestamp- t1.timestamp),3) as processing_time
from activity t1 join activity t2
on t1.machine_id = t2.machine_id
where t2.activity_type='end' and t1.activity_type='start'
group by t1.machine_id
