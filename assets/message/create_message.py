from telegram import ParseMode
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
import math

def create_mentor_card(db_data):
    card_mentor = '''
<strong>{} {}</strong> \n
Основной язык: <strong>{}</strong> 
Дополнительные языки: <strong>{}</strong> 
Ссылка на телеграм: <a href="{}">{}</a> 
    '''.format( \
        db_data[0], \
        db_data[1], \
        db_data[2], \
        db_data[3], \
        db_data[4], \
        db_data[4])
    return card_mentor

def question_card(quest_data):
    question = '''
Здравствуйте! Меня {} зовут. \n
Я извиняюсь если отвлекаю Вас,
но если есть свободная минутка помогите пожалуйста \n
В общем суть проблемы: {} \n
Краткое описание вопроса: {} \n
Дополнительная информация!
Основной язык на котором ведется разработка: {}
    '''.format(quest_data['name'], quest_data['title'], quest_data['question'], quest_data['lang'])
    return question

def mentors_card(obj):
    card = ''
    for i in range(len(obj)):
        card += '▫️ {} {} \n Основной язык: {}\n Дополнительные языки: {}\n Ссылка: {}\n\n'.format(
            obj[i][0], obj[i][1], obj[i][2], obj[i][3], obj[i][4])
    return card
    
