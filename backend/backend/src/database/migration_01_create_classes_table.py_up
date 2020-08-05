from connection import create_db_connection
import sys


def up(cursor):
    cursor.execute("""
            CREATE TABLE classes (
            id_class_pk SERIAL PRIMARY KEY,
            id_user_fk TEXT REFERENCES users(id_user_pk) NOT NULL,
            subject TEXT NOT NULL,
            cost TEXT NOT NULL
        )
    """)


def down(cursor):
    cursor.execute("DROP TABLE classes")


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
