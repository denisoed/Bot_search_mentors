from assets.messages import username, handler_reply_button
from assets.button.create_button import start_buttons


# Necessary variables
_user_name = '' 

# Start function
def hello(bot, update):
    update.message.reply_text(text=username['get_name'])

# Handler incoming messages
def message_processing(bot, update):
    message = update.message.text.encode('utf-8').decode('utf-8')
    if _user_name == '':
        global _user_name
        _user_name = update._effective_message.text
        bot.sendMessage(chat_id=update.message.chat_id, \
                        text=username['success_get_name'], reply_markup=start_buttons())
    else:
        for item in range(len(handler_reply_button)):
            if message == handler_reply_button[item]['name']:
                run = handler_reply_button[item]['run']
                run(bot, update, item)                
