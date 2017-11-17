from handlers.handler_db_queries import get_mentor
from telegram import ParseMode

def searching_mentor(bot, update, item, message):
    # update.message.reply_text(text=get_mentor(message))
    print(len(get_mentor(message)))
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=get_mentor(message), parse_mode=ParseMode.HTML)

def create_message():
    message = {}
    return message
