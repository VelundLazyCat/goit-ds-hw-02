--Знайти користувачів з певною електронною поштою
SELECT u.fullname, u.email 
FROM users u 
WHERE email LIKE  '%@example.org';