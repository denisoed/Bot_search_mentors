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
    mentors = []
    user = user.split(' ')
    for i in range(len(user)):
        cursor.execute('SELECT name, lastname, language, languages FROM Mentors WHERE {} LIKE "{}"'.format( \
            db_conf['tables_for_search'][i], str(user[i])))
        mentors.append(cursor.fetchall())

    cursor.close()
    conn.close()
    return str(mentors)
