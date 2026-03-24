Pandas Practice Datasets for Data Engineering

Files:
- customers.csv
- products.csv
- orders.csv
- order_items.csv
- web_events.csv
- inventory_snapshots.csv
- dirty_orders.csv

Suggested join keys:
- customers.customer_id -> orders.customer_id
- orders.order_id -> order_items.order_id
- products.product_id -> order_items.product_id
- products.product_id -> inventory_snapshots.product_id

Practice ideas:
1. Cleaning:
   - Fix null values, mixed date formats, extra spaces, wrong data types.
   - Remove duplicates from order_items.csv.
2. Analysis:
   - Revenue by month, city, channel, category.
   - Top customers by revenue and order count.
   - Conversion funnel using web_events.csv.
3. Data engineering tasks:
   - Build a fact table from orders + order_items + products + customers.
   - Create daily KPIs and write them to CSV.
   - Detect low-stock products using inventory_snapshots.csv.
   - Create reusable ETL functions.
