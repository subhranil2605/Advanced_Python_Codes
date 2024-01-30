import logging
import sqlite3
from contextlib import contextmanager


@contextmanager
def open_db(file_name: str):
    connection = sqlite3.connect(file_name)
    try:
        logging.info("Creating connection")
        cursor = connection.cursor()
        yield cursor
    except sqlite3.DatabaseError as error:
        logging.error(error)
    finally:
        logging.info("Closing connection")
        connection.commit()
        connection.close()


def main():
    logging.basicConfig(level=logging.INFO)
    with open_db(file_name="application.db") as cursor:
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())


if __name__ == '__main__':
    main()
