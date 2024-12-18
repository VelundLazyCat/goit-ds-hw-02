--Отримати список користувачів, які не мають жодного завдання.
SELECT u.id, u.fullname 
FROM users u 
WHERE u.id NOT IN 
(SELECT t.user_id 
FROM tasks t);