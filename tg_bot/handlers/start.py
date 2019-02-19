from tg_bot.models import Users
from django.template import loader


def start(bot, update):
    user = Users.objects.get
    update.message.reply_text('test')

