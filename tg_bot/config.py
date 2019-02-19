import os
from telegram import Bot
from telegram.ext import (Dispatcher, CommandHandler, MessageHandler, Filters,
                          CallbackQueryHandler, RegexHandler)
from tg_bot.handlers import start
from tg_bot.filters import basefilters
api_token = os.getenv('BOT_TOKEN')
robot = Bot(api_token)
dp = Dispatcher(robot, None, workers=0)


dp.add_handler(CommandHandler('start', start))

