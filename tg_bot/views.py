from django.http import JsonResponse
import json
from telegram import Update
from tg_bot.config import robot
from tg_bot.config import dp


def webhooks(request, bot_token):
    try:
        upd = Update.de_json(json.loads(request.body.decode("utf-8")), robot)
    except Exception as e:
        return JsonResponse({})
    dp.process_update(upd)
    return JsonResponse({}, status=200)

