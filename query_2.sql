--Вибрати завдання за певним статусом.

SELECT t.title, s.name
FROM tasks t
JOIN status s ON s.id = t.status_id 
WHERE s.name = 'new';
