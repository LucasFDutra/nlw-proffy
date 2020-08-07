from flask import jsonify
from src.database.connection import create_db_connection
from src.utils.convert_hour_to_minutes import convert
import uuid
import psycopg2.extras


class Classes():
    def index(self, request):
        try:
            query_params = dict(request.args)
            print(query_params)
            week_day = query_params['week_day']
            subject = query_params['subject']
            time = query_params['time']

            time = convert(time)

            connection = create_db_connection()
            cursor = connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)

            cursor.execute("""
                SELECT
                    s.id_class_schedule_pk as id,
                    c.subject,
                    c.cost,
                    u.id_user_pk as user_id,
                    u.name, u.avatar,
                    u.whatsapp,
                    u.bio
                FROM classes          c
                JOIN users            u ON c.id_user_fk = u.id_user_pk
                JOIN class_schedule   s ON s.id_class_fk = c.id_class_pk
                WHERE c.subject = %s AND s.from_time <= %s AND s.to_time > %s AND s.week_day = %s
            """, (subject, time, time, week_day))
            res = cursor.fetchall()
            cursor.close()
            connection.close()

            return jsonify(res)
        except:
            return jsonify({'error': 'missing filters to search classes'}), 400

    def create(self, request):
        data = request.json
        name, avatar, whatsapp, bio, subject, cost, schedule = data.values()
        try:
            id_user = uuid.uuid4().hex
            connection = create_db_connection()
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO USERS (id_user_pk, name, avatar, whatsapp, bio) VALUES (%s, %s, %s, %s, %s);
            """, (id_user, name, avatar, whatsapp, bio))

            cursor.execute("""
                INSERT INTO CLASSES (id_user_fk, subject, cost) VALUES (%s, %s, %s) RETURNING id_class_pk;
            """, (id_user, subject, cost))
            class_id = cursor.fetchone()

            for day in schedule:
                week_day, from_time, to_time = day.values()
                cursor.execute("""
                    INSERT INTO CLASS_SCHEDULE (id_class_fk, week_day, from_time, to_time) VALUES (%s, %s, %s, %s)
                """, (class_id, week_day, convert(from_time), convert(to_time)))

            connection.commit()
            cursor.close()
            connection.close()
            return jsonify({'Create': 'OK'}), 201
        except:
            connection.close()
            return jsonify({'Error': 'Unexpected error while creating new class'}), 400
