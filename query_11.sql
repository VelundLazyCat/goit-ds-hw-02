--11. Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
SELECT t.title, s.name, u.email 
FROM tasks t 
LEFT JOIN status s ON s.id  = t.status_id 
LEFT JOIN users u ON u.id = t.user_id
WHERE u.email LIKE '%@example.com';