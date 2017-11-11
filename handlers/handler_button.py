from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Handler click button
# def click_inline_button(bot, update):
#     query = update.callback_query
#     if query.data == 'hello':
#         keyboard = create_button(data.list_lang)
#         reply_markup = InlineKeyboardMarkup(keyboard)
#         bot.send_message(parse_mode='HTML', chat_id=query.message.chat_id,
#                         text='Выбери язык на котором ты пишешь?', reply_markup=reply_markup) 

# Create button
# def create_button(query):
#     keyboard = [[]]
#     for i in range(1, len(query)):
#         keyboard[0].append(InlineKeyboardButton(text=query[i], callback_data=query[i]))
#     return keyboard