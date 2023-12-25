# Write your MySQL query statement below


Select class
from Courses
Group by class
Having Count(Distinct(student)) >=5