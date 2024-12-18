--Отримати всі завдання, які ще не завершено.
SELECT t.title, t.status_id 
FROM tasks t 
JOIN status s ON s.id = t.status_id 
WHERE s.name != 'completed';