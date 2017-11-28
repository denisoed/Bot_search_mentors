import sqlite3
from config import db_config
from assets import message 
from assets import messages


def all_mentors():
    with sqlite3.connect(db_config.db_conf['name']) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Mentors')
        mentors = cursor.fetchall()
        length_mentors = len(mentors)
        return [mentors, length_mentors]

def get_mentor(user_data):
    with sqlite3.connect(db_config.db_conf['name']) as conn:
        cursor = conn.cursor()
        user = user_data.split(' ')
        if len(user) == 2:
            cursor.execute('SELECT name, lastname, language, languages, telegram \
                FROM {} WHERE {}="{}" AND {}="{}" OR {}="{}" AND {}="{}"'.format( \
                db_config.db_conf['table_name_for_mentors'], \
                db_config.db_conf['columns_for_search'][0], \
                str(user[0]), \
                db_config.db_conf['columns_for_search'][1], \
                str(user[1]), \
                db_config.db_conf['columns_for_search'][1], \
                str(user[0]), \
                db_config.db_conf['columns_for_search'][0], \
                str(user[1])))
            mentor = cursor.fetchall()
            if mentor == []:
                return messages.message_handler_db['not_name_and_surname']
            else:
                return message.create_message.create_mentor_card(mentor[0])
        elif len(user) == 1:
            cursor.execute('SELECT name, lastname, language, languages, telegram \
                FROM {} WHERE {}="{}" OR {}="{}"'.format( \
                db_config.db_conf['table_name_for_mentors'], \
                db_config.db_conf['columns_for_search'][0], \
                str(user[0]), \
                db_config.db_conf['columns_for_search'][1], \
                str(user[0])))
            mentor = cursor.fetchall()
            if mentor == []:
                return messages.message_handler_db['not_name_or_surname']
            else:
                return message.create_message.create_mentor_card(mentor[0])
        elif len(user) == 0:
            return messages.message_handler_db['is_empty']
        else:
            return messages.message_handler_db['not_correct']
