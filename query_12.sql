--12. Отримати список завдань, що не мають опису.
SELECT t.id, t.title, t.description 
FROM tasks t
WHERE t.description = '' OR t.description IS NULL;