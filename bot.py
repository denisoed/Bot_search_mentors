from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from handlers.handler_message import hello, message_processing
from handlers.handler_button import button_processing
import logging
import secret

updater = Updater(token=secret.TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(level=logging.DEBUG, \
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater.dispatcher.add_handler(CommandHandler('start', hello))
updater.dispatcher.add_handler( \
    MessageHandler(Filters.text, message_processing))

# handler click button
updater.dispatcher.add_handler( \
    CallbackQueryHandler(button_processing))

updater.start_polling()
updater.idle()
