-- top 3 average temps in July or August per city
SELECT city,avg(value) AS avg_temp FROM temperatures WHERE month IN (7,8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
