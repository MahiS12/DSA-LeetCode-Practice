# Write your MySQL query statement below

Select Max(t.num) as num
From ( Select num,Count(num)
     from MyNumbers
     Group by num
     Having Count(num) = 1
     ) as t