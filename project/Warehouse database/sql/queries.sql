-- select d.month, sum(f.total_amount)from dim_date d join fact_sales f
-- on d.date_id = f.date_id
-- group by d.month
-- order by d.month

select d.product_name,sum(f.total_amount) as total_amount from dim_product d join fact_sales f
on d.product_id = f.product_id 
group by d.product_name
order by total_amount desc
LIMIT 10;