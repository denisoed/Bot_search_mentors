import sqlite3
from config.db_config import db_conf
from assets.message.create_message import create_mentor_card

def all_mentors():
    with sqlite3.connect(db_conf['name']) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Mentors')
        mentors = cursor.fetchall()
        length_mentors = len(mentors)
        return [mentors, length_mentors]

def get_mentor(user_data):
    with sqlite3.connect(db_conf['name']) as conn:
        cursor = conn.cursor()
        user = user_data.split(' ')
        if len(user) == 2:
            cursor.execute('SELECT name, lastname, language, languages, telegram \
                FROM {} WHERE {}="{}" AND {}="{}" OR {}="{}" AND {}="{}"'.format( \
                db_conf['table_name_for_mentors'], \
                db_conf['columns_for_search'][0], \
                str(user[0]), \
                db_conf['columns_for_search'][1], \
                str(user[1]), \
                db_conf['columns_for_search'][1], \
                str(user[0]), \
                db_conf['columns_for_search'][0], \
                str(user[1])))
            mentor = cursor.fetchall()
            if mentor == []:
                return 'Ментор с таким Именем и Фамилией не найден!'
            else:
                return create_mentor_card(mentor[0])
        elif len(user) == 1:
            cursor.execute('SELECT name, lastname, language, languages, telegram \
                FROM {} WHERE {}="{}" OR {}="{}"'.format( \
                db_conf['table_name_for_mentors'], \
                db_conf['columns_for_search'][0], \
                str(user[0]), \
                db_conf['columns_for_search'][1], \
                str(user[0])))
            mentor = cursor.fetchall()
            if mentor == []:
                return 'Ментор с таким Именем или Фамилией не найден!'
            else:
                return create_mentor_card(mentor[0])
        elif len(user) == 0:
            return 'Введите данные'
        else:
            return 'Пожалуйста введите корректные данные'
