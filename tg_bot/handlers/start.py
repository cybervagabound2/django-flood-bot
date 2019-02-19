from tg_bot.models import Users
from django.template import loader


def start(bot, update):
    user = add_user(update)
    user.params = ''
    user.save()
    msg = loader.get_template('tg_bot/start.html').render()
    user.send_message(bot, msg=msg)


def add_user(update):
    user = Users.objects.filter(telegram_id=update.message.chat.id)
    if user.count() is 0:
        invated = update.message.text.split(' ')
        if len(invated) > 1 and invated[1] != str(update.message.from_user.id):
            invated_user = Users.objects.filter(telegram_id=invated[1])
            if invated_user.count() != 0:
                invated_user = invated_user.get(telegram_id=invated[1])
                user = Users(telegram_id=update.message.chat.id, username=update.message.chat.username,
                             first_name=update.message.chat.first_name, last_name=update.message.chat.last_name,
                             invited_by=invated_user.id)
                user.save()
                return
        user = Users(telegram_id=update.message.chat.id, username=update.message.chat.username,
                     first_name=update.message.chat.first_name, last_name=update.message.chat.last_name)
        user.save()
    else:
        user = user.get(telegram_id=update.message.chat.id)
        user.first_name = update.message.chat.first_name
        user.last_name = update.message.chat.last_name
        user.username = update.message.chat.username
        user.params = '[]'
        user.blocked = False
        user.save()
    return user
