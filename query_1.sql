--Отримати всі завдання певного користувача.
SELECT t.user_id, t.title
FROM tasks t 
WHERE t.user_id  = 2;