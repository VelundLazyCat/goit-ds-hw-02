import sqlite3
import logging
from sqlite3 import DatabaseError, Error


def execute_query(sql_file: str) -> list:
    # читаємо файл зі скриптом для запиту до БД
    try:
        with open(sql_file, 'r') as f:
            sql_query = f.read()
    except FileNotFoundError as e:
        logging.error(e)

    with sqlite3.connect('grades.db') as conn:
        try:
            cur = conn.cursor()
            cur.execute(sql_query)
        except DatabaseError as e:
            logging.error(e)
            cur.close()
        return cur.fetchall()


def print_query(query_file, text=None):
    result = execute_query(query_file)
    print(text)
    print(result)
    print('*' * 30)


def query_3(*parameters):

    sql = ''' 
    UPDATE tasks
    SET status_id = ? 
    WHERE id = ?
    '''
    with sqlite3.connect('tasks.db') as conn:
        try:
            cur = conn.cursor()
            cur.execute(sql, parameters)
            conn.commit()
        except Error as e:
            logging.error(e)
        finally:
            cur.close()


def query_5(*parameters):

    sql = ''' 
    INSERT INTO tasks (title, description, status_id, user_id)
    VALUES (?, ?, ?, ?)
    '''
    with sqlite3.connect('tasks.db') as conn:
        try:
            cur = conn.cursor()
            cur.execute(sql, parameters)
            conn.commit()
        except Error as e:
            logging.error(e)
        finally:
            cur.close()


def query_9(*parameters):
    sql = ''' 
    UPDATE users 
    SET fullname = ?
    WHERE id = ?    
    '''
    with sqlite3.connect('tasks.db') as conn:
        try:
            cur = conn.cursor()
            cur.execute(sql, parameters)
            conn.commit()
        except Error as e:
            logging.error(e)
        finally:
            cur.close()


if __name__ == "__main__":

    # 1. Отримати всі завдання певного користувача.
    print_query('query_1.sql', "1. Отримати всі завдання певного користувача.")

    # 2. Вибрати завдання за певним статусом.
    print_query('query_2.sql', "2. Вибрати завдання за певним статусом.")

    # 3. Оновити статус конкретного завдання. Змінюємо для завдання №2 статус на 1
    query_3(1, 2)

    # 4. Отримати список користувачів, які не мають жодного завдання.
    print_query(
        'query_4.sql', "4. Отримати список користувачів, які не мають жодного завдання.")

    # 5. Додати нове завдання для конкретного користувача.
    query_5("сходити в магазин", "купити цукор і макарони", 1, 2)

    # 6. Отримати всі завдання, які ще не завершено.
    print_query('query_6.sql', "6. Отримати всі завдання, які ще не завершено.")

    # 7. Видалити конкретне завдання (візьмемо завдання з id=4).
    execute_query('query_7.sql')

    # 8. Знайти користувачів з певною електронною поштою.
    print_query('query_8.sql',
                "8. Знайти користувачів з певною електронною поштою.")

    # 9. Оновити ім'я користувача.
    query_9('Кіт Степан', 2)

    # 10. Отримати кількість завдань для кожного статусу.
    print_query('query_10.sql',
                "10. Отримати кількість завдань для кожного статусу.")

    # 11. Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
    print_query('query_11.sql',
                "11. Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.")

    # 12. Отримати список завдань, що не мають опису.
    print_query('query_12.sql',
                "Отримати список завдань, що не мають опису.")

    # 13. Вибрати користувачів та їхні завдання, які є у статусі 'in progress'.
    print_query('query_13.sql',
                "13. Вибрати користувачів та їхні завдання, які є у статусі 'in progress'")

    # 14. Отримати користувачів та кількість їхніх завдань.
    print_query('query_14.sql',
                "14. Отримати користувачів та кількість їхніх завдань.")
