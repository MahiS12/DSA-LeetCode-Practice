# Write your MySQL query statement below

select t1.year, t1.price, t2.product_name
from Sales t1 left join Product t2
on t1.product_id = t2.product_id