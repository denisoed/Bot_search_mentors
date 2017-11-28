import math
from handlers import handler_db_queries
from .message import create_message
from telegram import ParseMode
from .button import create_button
from . import messages

_MAIN_GLOB_VAR = {
    'counter_output_mentors': 0
}

_QUESTION = {
    'name': '',
    'title': '',
    'question': '',
    'lang': ''
}

def get_all_mentors(bot, update, item, message):

    global _MAIN_GLOB_VAR
    total_item = int(len(handler_db_queries.all_mentors()[0]))
    step = 3
    page = int(math.ceil(total_item / step))

    def get_pages():
        counter = 0
        array_page = []
        for i in range(page):
            array_page.append([])
            for j in range(step):
                array_page[i].append(handler_db_queries.all_mentors()[0][counter])
                counter += 1    
        return array_page
    
    if message == 'Все менторы':
        bot.send_message(chat_id=update.message.chat_id, \
                         text=create_message.mentors_card(get_pages()[0]),
                         reply_markup=create_button.slide_mentors(bot, update, item, message))
        _MAIN_GLOB_VAR['counter_output_mentors'] += 1

    elif message == 'yet':
        try:
            bot.send_message(chat_id=update.callback_query.message.chat_id, \
                             text=create_message.mentors_card(
                                 get_pages()[_MAIN_GLOB_VAR['counter_output_mentors']]),
                            reply_markup=create_button.slide_mentors(bot, update, item, message))
            _MAIN_GLOB_VAR['counter_output_mentors'] += 1
        except IndexError:
            bot.send_message(chat_id=update.callback_query.message.chat_id, \
                            text='Больше нету!')


def searching_mentor(bot, update, item, message):
    bot.sendMessage(chat_id=update.message.chat_id, \
                    text=handler_db_queries.get_mentor(message), parse_mode=ParseMode.HTML)


def creating_question(bot, update, item, message):
    global _QUESTION
    if _QUESTION['name'] == '':
        _QUESTION['name'] = message
        bot.sendMessage(chat_id=update.message.chat_id,
                        text=messages.question_data['title'], parse_mode=ParseMode.HTML)
    elif _QUESTION['title'] == '':
        _QUESTION['title'] = message
        bot.sendMessage(chat_id=update.message.chat_id,
                        text=messages.question_data['the_problem'], parse_mode=ParseMode.HTML)
    elif _QUESTION['question'] == '':
        _QUESTION['question'] = message
        bot.sendMessage(chat_id=update.message.chat_id,
                        text=messages.question_data['lang'], parse_mode=ParseMode.HTML)
    elif _QUESTION['lang'] == '':
        _QUESTION['lang'] = message
        bot.sendMessage(chat_id=update.message.chat_id,
                        text=create_message.question_card(_QUESTION), parse_mode=ParseMode.HTML)
        message = messages.question_data['data']                
        create_button.start_buttons(bot, update, item, message)
