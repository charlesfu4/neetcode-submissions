-- Write your query below


select distinct name 
from customers left join orders
on customers.id = orders.customer_id
where orders.id is null;