from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from assets import messages

# Start button
def start_buttons():
    fast_search = InlineKeyboardButton(text="Быстрый поиск")
    button = InlineKeyboardButton(text="Узнать погоду")
    keyboard = [[fast_search, button]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    return reply_markup

# Start button
def search_mentor_btn(bot, update, item):
    search = InlineKeyboardButton(text="Найти")
    keyboard = [[search]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = bot.sendMessage(chat_id=update.message.chat_id, \
                           text=messages.handler_reply_button[item]['text'], reply_markup=reply_markup)
    return send

