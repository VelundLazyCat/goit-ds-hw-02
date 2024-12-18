--14. Отримати користувачів та кількість їхніх завдань.
SELECT t.user_id,  u.fullname , COUNT(t.title) AS quontity_tasks
FROM tasks t 
JOIN users u ON u.id = t.user_id 
GROUP BY t.user_id;