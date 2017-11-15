from assets.messages import username, handler_reply_button
from assets.button.create_button import start_buttons
from assets.main import searching_mentor


# Necessary variables
_user_name = '' 
_search = ''

# Start function
def hello(bot, update):
    update.message.reply_text(text=username['get_name'])


# Handler incoming messages
def message_processing(bot, update):
    # btn_callback_msg = update.message.text.encode('utf-8').decode('utf-8')
    btn_callback_msg = update._effective_message.text
    if _user_name == '':
        global _user_name
        _user_name = update._effective_message.text
        bot.sendMessage(chat_id=update.message.chat_id, \
                        text=username['success_get_name'], reply_markup=start_buttons())
    else:
        if update._effective_message.text != 'Найти':
            global _search
            _search = update._effective_message.text
            for item in range(len(handler_reply_button)):
                if btn_callback_msg == handler_reply_button[item]['name']:
                    run = handler_reply_button[item]['run']
                    run(bot, update, item, _search)
        else:    
            for item in range(len(handler_reply_button)):
                if btn_callback_msg == handler_reply_button[item]['name']:
                    run = handler_reply_button[item]['run']
                    run(bot, update, item, _search)
