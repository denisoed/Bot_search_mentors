from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from assets import messages

# Start button
def start_buttons():
    fast_search = InlineKeyboardButton(text="Быстрый поиск")
    help_btn = InlineKeyboardButton(text="Помочь")
    keyboard = [[fast_search, help_btn]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    return reply_markup

# Button to start serching mentors
def search_mentor_btn(bot, update, item, message):
    search = InlineKeyboardButton(text="Найти")
    keyboard = [[search]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = bot.sendMessage(chat_id=update.message.chat_id, \
                           text=messages.handler_reply_button[item]['text'], reply_markup=reply_markup)
    return send

# Button slide 
def help_slide_btn(bot, update, item, message):
    prev_btn = InlineKeyboardButton(text="Назад")
    next_btn = InlineKeyboardButton(text="Дальше")
    keyboard = [[prev_btn, next_btn]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    send = bot.sendMessage(chat_id=update.message.chat_id,
                           text=messages.handler_reply_button[item]['text'], reply_markup=reply_markup)
    return send
