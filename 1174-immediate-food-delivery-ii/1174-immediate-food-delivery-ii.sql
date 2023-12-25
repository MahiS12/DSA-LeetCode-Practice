# Write your MySQL query statement below


# Select ROUND(AVG(order_date =customer_pref_delivery_date)*100 ,2) as immediate_percentage
# from Delivery
# Where (customer_id,order_date) in (
# Select customer_id, min(order_date)
# from Delivery
# Group by customer_id
# )

select round(count(t1.customer_id )/(select count(distinct customer_id ) from Delivery) *100,2) 
as immediate_percentage  
from (
    select customer_id 
    from Delivery 
    group by customer_id 
    having min(order_date)=min(customer_pref_delivery_date)
) as t1