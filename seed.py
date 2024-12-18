import sqlite3
import logging
from faker import Faker
import random
from sqlite3 import DatabaseError


NUMBER_USERS = 40
STATUS = [('new',), ('in progress',), ('completed',)]
NUMBER_TASKS = 30


def insert_data_to_db(sql_query: str, variables: list) -> None:

    with sqlite3.connect('tasks.db') as conn:
        try:
            cur = conn.cursor()
            cur.executemany(sql_query, variables)
            logging.debug(f'База оновлена, додано {len(variables)} строк')
        except DatabaseError as e:
            logging.error(e)
            conn.rollback()
            cur.close()


def fill_db(*args: list) -> None:

    sql_fill = ["""INSERT INTO users(fullname, email) VALUES (?, ?);""",
                """INSERT INTO status(name) VALUES (?);""",
                """INSERT INTO tasks(title, description, status_id, user_id) VALUES (?, ?, ?, ?);""",
                ]

    for num, vars in enumerate(args):
        insert_data_to_db(sql_fill[num], vars)
    logging.debug('Заповнення бази данних виконано.')


def generate_fake_data(number_users, status, number_tasks) -> tuple:
    fake_users = []  # тут зберігатимемо користувачів
    fake_status = []  # тут зберігатимемо статуси завдань
    fake_tasks = []  # тут зберігатимемо завдання

    fake_data = Faker('uk-UA')

    # створення користувачів
    for _ in range(number_users):
        fake_users.append((fake_data.name(), fake_data.email()))

    # створення статусів завдань
    for s in status:
        fake_status.append((s,))

    # створення назв і описів завдань
    for _ in range(number_tasks):
        status_id = random.randint(1, len(status))
        user_id = random.randint(1, number_users)
        fake_tasks.append(
            (fake_data.word(), fake_data.sentence(), status_id, user_id))
        print(fake_data.word(), fake_data.sentence(), status_id, user_id)

    return fake_users, status, fake_tasks


if __name__ == "__main__":
    logging.DEBUG
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)
    fill_db(*generate_fake_data(NUMBER_USERS, STATUS, NUMBER_TASKS))
