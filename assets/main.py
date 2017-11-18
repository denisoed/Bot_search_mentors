from handlers.handler_db_queries import get_mentor, all_mentors
from telegram import ParseMode
from .message.create_message import create_mentor_card

def get_all_mentors(bot, update, item, message):
    bot.sendMessage(chat_id=update.message.chat_id, \
                    text=str(all_mentors()[0]), parse_mode=ParseMode.HTML)
                    
def searching_mentor(bot, update, item, message):
    bot.sendMessage(chat_id=update.message.chat_id, \
                    text=get_mentor(message), parse_mode=ParseMode.HTML)
