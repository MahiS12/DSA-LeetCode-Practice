# Write your MySQL query statement below

Select product_id, 10 as price
from Products
Group by product_id
Having Min(change_date) > "2019-08-16"  #if it is changing after the given date, the price on this date was 10
Union
select product_id, new_price as price
from Products
where (product_id,change_date) in (
    select product_id, max(change_date)
    from Products
    where change_date <= "2019-08-16"  
    group by product_id

)