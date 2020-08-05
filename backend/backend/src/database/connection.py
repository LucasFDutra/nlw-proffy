import psycopg2
import os


def create_db_connection():
    connection_params = {
        'dbname': os.environ['PROFFY_DBNAME'],
        'user': os.environ['PROFFY_USER'],
        'password': os.environ['PROFFY_PASSWORD'],
        'host': os.environ['PROFFY_HOST'],
        'port': os.environ['PROFFY_PORT']
    }
    connection = psycopg2.connect(**connection_params)
    return connection
