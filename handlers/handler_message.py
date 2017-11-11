from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from . import data
from assets import messages

def hello(bot, update):
    update.message.reply_text(messages.get_name)

# Handler queries
def message_processing(bot, update):
    print(update._effective_message.text)
