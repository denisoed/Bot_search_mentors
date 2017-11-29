from assets import messages
from assets.button import create_button


# Necessary variables
_USER_NANE = ''
_MESSAGE = ''

# Start function
def hello(bot, update):
    create_button.start_buttons( \
        bot, update, 0, messages.message_instruction['start_btn_instruction'])


# Handler incoming messages
def message_processing(bot, update):
    btn_callback_msg = update._effective_message.text
    if update._effective_message.text == 'Найти':
        run(bot, update, btn_callback_msg)
    elif update._effective_message.text == 'Дальше':
        run(bot, update, btn_callback_msg)
    elif update._effective_message.text == 'Назад':
        run(bot, update, btn_callback_msg)
    else:
        global _MESSAGE
        _MESSAGE = update._effective_message.text
        run(bot, update, btn_callback_msg)


def run(bot, update, btn_callback_msg):
    for item in range(len(messages.handler_reply_button)):
        if btn_callback_msg == messages.handler_reply_button[item]['name']:
            run = messages.handler_reply_button[item]['run']
            run(bot, update, item, _MESSAGE)
