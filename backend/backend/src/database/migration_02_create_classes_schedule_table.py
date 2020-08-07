from connection import create_db_connection
import sys


def up(cursor):
    cursor.execute("""
            CREATE TABLE class_schedule (
            id_class_schedule_pk SERIAL PRIMARY KEY,
            id_class_fk INTEGER REFERENCES classes(id_class_pk) NOT NULL,
            week_day INTEGER NOT NULL,
            from_time INTEGER NOT NULL,
            to_time INTEGER NOT NULL
        )
    """)


def down(cursor):
    cursor.execute("DROP TABLE class_schedule")


if __name__ == "__main__":
    connection = create_db_connection()
    cursor = connection.cursor()

    if ('--up' in sys.argv):
        up(cursor)
    if ('--down' in sys.argv):
        down(cursor)

    connection.commit()
    cursor.close()
    connection.close()
