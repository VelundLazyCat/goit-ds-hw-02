--13. Вибрати користувачів та їхні завдання, які є у статусі 'in progress'.
SELECT u.fullname, t.title, s.name
FROM tasks t
JOIN users u ON u.id = t.user_id
INNER JOIN status s ON s.id = t.status_id 
WHERE s.name LIKE 'in progress';