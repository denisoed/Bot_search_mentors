from assets.messages import username, handler_reply_button
from assets.button.create_button import start_buttons
from assets.main import searching_mentor


# Necessary variables
_USER_NANE = '' 
_message = ''

# Start function
def hello(bot, update):
    start_buttons(bot, update, 0, username['success_get_name'])
    update.message.reply_text(text=username['get_name'])


# Handler incoming messages
def message_processing(bot, update):
    btn_callback_msg = update._effective_message.text
    if update._effective_message.text == 'Найти':
        for item in range(len(handler_reply_button)):
            if btn_callback_msg == handler_reply_button[item]['name']:
                run = handler_reply_button[item]['run']
                run(bot, update, item, _message)
    if update._effective_message.text == 'Дальше':
        for item in range(len(handler_reply_button)):
            if btn_callback_msg == handler_reply_button[item]['name']:
                run = handler_reply_button[item]['run']
                run(bot, update, item, _message)
    else:    
        global _message
        _message = update._effective_message.text
        for item in range(len(handler_reply_button)):
            if btn_callback_msg == handler_reply_button[item]['name']:
                run = handler_reply_button[item]['run']
                run(bot, update, item, _message)
