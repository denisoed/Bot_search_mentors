import sqlite3
from config.db_config import db_conf

def all_mentors():
    conn = sqlite3.connect(db_conf['name'])
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Mentors')
    mentors = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return mentors[0][0]

def get_mentor(user_data):
    with sqlite3.connect(db_conf['name']) as conn:
        cursor = conn.cursor()
        mentors = ''
        user = user_data.split(' ')
        if len(user) == 2:
            cursor.execute('SELECT name, lastname, language, languages \
                FROM Mentors WHERE {}="{}" AND {}="{}" OR {}="{}" AND {}="{}"'.format( \
                db_conf['tables_for_search'][0], str(user[0]), db_conf['tables_for_search'][1], str(user[1]), \
                db_conf['tables_for_search'][1], str(user[0]), db_conf['tables_for_search'][0], str(user[1])))
            mentors = cursor.fetchall()
            if mentors == []:
                return 'Ментор с таким Именем и Фамилией не найден!'
            else:
                card_mentor = '''
            Ментор: <strong>{}</strong> 
            '''.format(mentors)
                return str(card_mentor)
        elif len(user) == 1:
            cursor.execute('SELECT name, lastname, language, languages FROM Mentors WHERE {}="{}" OR {}="{}"'.format(
                db_conf['tables_for_search'][0], str(user[0]), db_conf['tables_for_search'][1], str(user[0])))
            mentors = cursor.fetchall()
            if mentors == []:
                return 'Ментор с таким Именем или Фамилией не найден!'
            else:
                card_mentor = '''
            Ментор: <strong>{}</strong> 
            '''.format(mentors)
                return str(card_mentor)
        elif len(user) == 0:
            return 'Введите данные'        
        else:
            return 'Пожалуйста введите корректные данные'
