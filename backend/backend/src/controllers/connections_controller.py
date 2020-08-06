from flask import jsonify
from src.database.connection import create_db_connection
from src.utils.convert_hour_to_minutes import convert
import psycopg2.extras


class ConnectionsController():
    def index(self, request):
        connection = create_db_connection()
        cursor = connection.cursor()

        cursor.execute("""
            select count(*) from connections;
        """)
        res = cursor.fetchone()[0]

        cursor.close()
        connection.close()
        return jsonify({'total': res})

    def create(self, request):
        try:
            connection = create_db_connection()
            cursor = connection.cursor()

            id_user = request.json['user_id']

            cursor.execute("""
                INSERT INTO CONNECTIONS (id_user_fk) VALUES (%s)
            """, (id_user,))

            connection.commit()
            cursor.close()
            connection.close()

            return jsonify({'Create': 'OK'}), 201
        except:
            return jsonify({'error': 'failed to create new connection'}), 401
