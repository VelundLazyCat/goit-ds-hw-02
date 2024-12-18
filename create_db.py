import sqlite3
import logging
from sqlite3 import DatabaseError


logging.DEBUG
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)


def create_db() -> None:
    # читаємо файл зі скриптом для створення БД
    try:
        with open('query_create_db.sql', 'r') as f:
            sql = f.read()
    except FileNotFoundError as e:
        logging.error(e)

    with sqlite3.connect('tasks.db') as conn:
        try:
            cur = conn.cursor()
            # виконуємо скрипт який створить таблиці в БД
            cur.executescript(sql)
            logging.debug('база створена')
        except DatabaseError as e:
            logging.error('p1', e)
            conn.rollback()
            cur.close()


if __name__ == "__main__":
    create_db()
