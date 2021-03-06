import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from handlers.handler_message import hello, message_processing
from handlers.handler_button import button_processing
import secret

_UPDATER = Updater(token=secret.TOKEN)

logging.basicConfig(level=logging.DEBUG, \
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# handler send command(=> /start <=)
_UPDATER.dispatcher.add_handler(CommandHandler('start', hello))

# handler send message
_UPDATER.dispatcher.add_handler(MessageHandler(Filters.text, message_processing))

# handler click button
_UPDATER.dispatcher.add_handler(CallbackQueryHandler(button_processing))

_UPDATER.start_polling()
_UPDATER.idle()
