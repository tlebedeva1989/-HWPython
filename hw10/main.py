from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import user_interface

token1 = "6219208718:AAHyatt1K0m06BTdEZhrbUZtqs9c1H6JZe0"

bot = Bot(token="6219208718:AAHyatt1K0m06BTdEZhrbUZtqs9c1H6JZe0")
updater = Updater(token=token1)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', user_interface.start)
getmes_handler = MessageHandler(Filters.text, user_interface.get_message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(getmes_handler)

updater.start_polling()
updater.idle()