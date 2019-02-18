from telegram import Bot
from telegram.ext import (Dispatcher, CommandHandler, MessageHandler, Filters,
                          CallbackQueryHandler, RegexHandler)
from tg.handlers.start import start
from tg.handlers.start import error
from tg.filters import basefilters
api_token = ''
robot = Bot(api_token)
dp = Dispatcher(robot, None, workers=4)


dp.add_handler(CommandHandler('start', start))
dp.add_error_handler(error)

