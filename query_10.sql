--Отримати кількість завдань для кожного статусу.
SELECT s.name AS task_name, COUNT(*) AS quontity_tasks
FROM tasks t 
JOIN status s ON s.id = t.status_id 
GROUP BY t.status_id;