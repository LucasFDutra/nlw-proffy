from connection import create_db_connection
import sys


def up(cursor):
    cursor.execute("""
            CREATE TABLE connections (
            id_connections_pk SERIAL PRIMARY KEY,
            id_user_fk TEXT REFERENCES users(id_user_pk) NOT NULL,
            created_at DATE DEFAULT current_timestamp NOT NULL
        )
    """)


def down(cursor):
    cursor.execute("DROP TABLE connections")


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
