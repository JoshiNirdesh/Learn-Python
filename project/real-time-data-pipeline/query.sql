-- Top sources by articles
SELECT source_id, COUNT(*) AS total_articles
FROM fact_news
GROUP BY source_id
ORDER BY total_articles DESC;

-- Articles per day
SELECT d.year, d.month, COUNT(*) 
FROM fact_news f
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY d.year, d.month;