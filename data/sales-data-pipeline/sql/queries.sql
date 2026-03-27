-- Total sales by city
SELECT city, SUM(total_amount) AS total_sales
FROM sales
GROUP BY city
ORDER BY total_sales DESC;

-- Total sales by category
SELECT category, SUM(total_amount) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC;

-- Top 10 customers
SELECT customer_name, SUM(total_amount) AS total_spent
FROM sales
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 10;

-- Monthly sales trend
SELECT DATE_TRUNC('month', order_date) AS month, SUM(total_amount) AS monthly_sales
FROM sales
GROUP BY month
ORDER BY month;

-- Payment method usage
SELECT payment_method, COUNT(*) AS usage_count
FROM sales
GROUP BY payment_method
ORDER BY usage_count DESC;