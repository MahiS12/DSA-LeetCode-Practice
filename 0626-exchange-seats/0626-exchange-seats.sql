# Write your MySQL query statement below

Select case
when s.id %2 <>0 and s.id = (select max(id) from Seat) then s.id #if last id
when s.id % 2 = 0 then s.id - 1 #if id is even then swap with prev
else s.id +1 #if id is odd then swap with next
end
as id, student
from Seat as s
Order by id ASC