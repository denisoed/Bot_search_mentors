from handlers.handler_db_queries import get_mentor

def searching_mentor(bot, update, item, message):
    update.message.reply_text(text=get_mentor(message))

def create_message():
    message = {}
    return message
