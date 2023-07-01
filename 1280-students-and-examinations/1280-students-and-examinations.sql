# Write your MySQL query statement below

select t1.student_id, t1.student_name, sub.subject_name, count(t2.student_id) as attended_exams
from Students t1 cross join Subjects sub
left join Examinations t2
on t1.student_id = t2.student_id and sub.subject_name = t2.subject_name
group by t1.student_id, t1.student_name, sub.subject_name
order by t1.student_id,sub.subject_name

