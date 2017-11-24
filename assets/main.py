from handlers.handler_db_queries import get_mentor, all_mentors
from .message.create_message import create_mentor_card, create_all_mentor_card
from telegram import ParseMode
from .button.create_button import slide_mentors, send_question, start_buttons
from . import messages
import math

_MAIN_GLOB_VAR = {
    'counter_output_mentors': 0
}

_QUESTION = {
    'lang': '',
    'question': ''
}

def get_all_mentors(bot, update, item, message):

    global _MAIN_GLOB_VAR
    total_item = int(len(all_mentors()[0]))
    step = 3
    page = int(math.ceil(total_item / step))

    def get_pages():
        counter = 0
        array_page = []
        for i in range(page):
            array_page.append([])
            for j in range(step):
                array_page[i].append(all_mentors()[0][counter])
                counter += 1    
        return array_page
    
    if message == 'Все менторы':
        bot.send_message(chat_id=update.message.chat_id, \
                         text=messages.mentors_card(get_pages()[0]),
                         reply_markup=slide_mentors(bot, update, item, message))
        _MAIN_GLOB_VAR['counter_output_mentors'] += 1

    elif message == 'yet':
        try:
            bot.send_message(chat_id=update.callback_query.message.chat_id, \
                             text=messages.mentors_card(
                                 get_pages()[_MAIN_GLOB_VAR['counter_output_mentors']]),
                            reply_markup=slide_mentors(bot, update, item, message))
            _MAIN_GLOB_VAR['counter_output_mentors'] += 1
        except IndexError:
            bot.send_message(chat_id=update.callback_query.message.chat_id, \
                            text='Больше нету!')


def searching_mentor(bot, update, item, message):
    bot.sendMessage(chat_id=update.message.chat_id, \
                    text=get_mentor(message), parse_mode=ParseMode.HTML)


def creating_question(bot, update, item, message):
    global _QUESTION
    if _QUESTION['lang'] == '':
        _QUESTION['lang'] = message
        bot.sendMessage(chat_id=update.message.chat_id,
                        text='Опишите коротко свой вопрос', parse_mode=ParseMode.HTML)
    if _QUESTION['question'] == '':
        _QUESTION['question'] = message
        bot.sendMessage(chat_id=update.message.chat_id,
                        text=messages.question_card(_QUESTION), parse_mode=ParseMode.HTML)
        start_buttons(bot, update, item, message)
