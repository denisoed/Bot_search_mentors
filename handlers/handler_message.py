from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from . import data
from assets import messages


# Necessary variables
user_name = '' 

# Start function
def hello(bot, update):
    update.message.reply_text(messages.get_name)
                       
# Handler incoming messages
def message_processing(bot, update):
    if user_name == '':
        get_user_name(update)
        update.message.reply_text(text='Ну привет %s' % user_name)
    else:
        update.message.reply_text(text=messages.unknown_message)

# Get user name
def get_user_name(update):
    global user_name
    user_name = update._effective_message.text
