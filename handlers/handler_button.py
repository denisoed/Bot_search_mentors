from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


# Handler click button
def button_processing(bot, update):
    pass
    # query = update.callback_query 
    # print(query)
    # if query.data == 'search_mentor_name':
    #     reply_keyboard = [['Boy', 'Girl', 'Other']]

    #     bot.sendMessage(
    #         chat_id=query.message.chat.id,
    #         text='Hi! My name is Professor Bot. I will hold a conversation with you. '
    #         'Send /cancel to stop talking to me.\n\n'
    #         'Are you a boy or a girl?',
    #         reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

# Create button
# def create_button(query):
#     keyboard = [[]]
#     for i in range(1, len(query)):
#         keyboard[0].append(InlineKeyboardButton(text=query[i], callback_data=query[i]))
#     return keyboard
