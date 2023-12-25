# Write your MySQL query statement below

SELECT SUBSTR(trans_date,1,7) as month, country, count(id) as trans_count,  SUM(IF(state = 'approved',1,0)) AS approved_count, SUM(amount) as trans_total_amount, 
SUM(if(state = 'approved',amount,0)) as approved_total_amount
FROM Transactions
group by month,country


# DATE_FORMAT(trans_date, '%Y-%m') AS month