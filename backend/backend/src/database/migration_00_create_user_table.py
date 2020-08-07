from connection import create_db_connection
import sys


def up(cursor):
    cursor.execute("""
            CREATE TABLE users (
            id_user_pk TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            avatar TEXT NOT NULL,
            whatsapp TEXT NOT NULL,
            bio TEXT NOT NULL
        )
    """)


def down(cursor):
    cursor.execute("DROP TABLE users")


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
