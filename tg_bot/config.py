from telegram import Bot
from telegram.ext import (Dispatcher, CommandHandler, MessageHandler, Filters,
                          CallbackQueryHandler, RegexHandler)
from tg_bot.handlers import start
from tg_bot.filters import basefilters
api_token = '622052405:AAFJ6fYX-v-Hvt4TNd4M6n-CQD2huB-zStU'
robot = Bot(api_token)
dp = Dispatcher(robot, None, workers=4)


dp.add_handler(CommandHandler('start', start))

