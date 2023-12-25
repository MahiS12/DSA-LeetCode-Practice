# Write your MySQL query statement below


select product_id, year as first_year, quantity, price
from Sales
Where (product_id, year) in (
    select product_id, min(year)
    from Sales
    Group by product_id
)