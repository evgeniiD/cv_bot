
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import logging
from cv_bot import handlers, mytoken

TOKEN = mytoken.TOKEN
updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

start_handler = CommandHandler('start', handlers.start)
dispatcher.add_handler(start_handler)

updater.dispatcher.add_handler(CallbackQueryHandler(handlers.button_for_start_bio, pattern='start bio'))

updater.dispatcher.add_handler(CallbackQueryHandler(handlers.button_to_calm_down, pattern='^calm_down$'))

updater.dispatcher.add_handler(CallbackQueryHandler(handlers.about_front, pattern='^front$'))

updater.dispatcher.add_handler(CallbackQueryHandler(handlers.about_IB, pattern='^IB$'))

updater.dispatcher.add_handler(CallbackQueryHandler(handlers.about_back, pattern='^back$'))

updater.dispatcher.add_handler(CallbackQueryHandler(handlers.about_aws, pattern='^AWS$'))

updater.dispatcher.add_handler(CallbackQueryHandler(handlers.go_next, pattern='^go_next$'))

updater.dispatcher.add_handler(CallbackQueryHandler(handlers.brief_bio, pattern='^brief_bio$'))

updater.start_polling()