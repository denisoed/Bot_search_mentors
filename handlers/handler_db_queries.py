import sqlite3
from config.db_config import db_conf

def get_all_mentors():
    conn = sqlite3.connect(db_conf['name'])
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Mentors')
    mentors = cursor.fetchall()

    cursor.close()
    conn.close()
    return mentors

def get_mentor(user):
    conn = sqlite3.connect(db_conf['name'])
    cursor = conn.cursor()
    mentors = ''
    user = user.split(' ')
    if len(user) == 2:
        cursor.execute('SELECT name, lastname, language, languages FROM Mentors WHERE {}="{}" AND {}="{}"'.format( \
            db_conf['tables_for_search'][0], str(user[0]), db_conf['tables_for_search'][1], str(user[1])))
        mentors = cursor.fetchall()
    elif len(user) == 1:
        cursor.execute('SELECT name, lastname, language, languages FROM Mentors WHERE {}="{}" OR {}="{}"'.format(
            db_conf['tables_for_search'][0], str(user[0]), db_conf['tables_for_search'][1], str(user[0])))
        mentors = cursor.fetchall()

    cursor.close()
    conn.close()
    card_mentor = '''
Ментор: <strong>{}</strong> 
'''.format(mentors)
    return str(card_mentor)
