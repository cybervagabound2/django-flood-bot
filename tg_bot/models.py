from django.db import models


class Users(models.Model):
    ROLES = (
        ('ad', 'administrator'),
        ('us', 'user')
    )
    telegram_id = models.IntegerField()
    username = models.CharField(max_length=32, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    params = models.CharField(max_length=1000, default='[]')
    last_message_id = models.CharField(max_length=255, null=True)
    role = models.CharField(max_length=2, default='us', choices=ROLES)

    def del_end_params(self, count=0):
        if count == 0:
            index = self.params.rfind('/')
            self.params = self.params[:index]
        else:
            while count != 0:
                index = self.params.rfind('/')
                self.params = self.params[:index]
                count -= 1
        self.save

    def get_end_params(self):
        index = self.params.rfind('/')
        return self.params[index:]

    def send_message(self, bot, msg, keyboard=None, photo=None, save_message_id=None):
        """Кастомный метод для отправки сообщения пользователю."""
        try:
            if self.last_message_id:
                bot.delete_message(chat_id=self.telegram_id, message_id=self.last_message_id)
                self.last_message_id = None
                self.save()
        except Exception as e:
            self.Error(bot, e, 'bot.delete_message')
        try:
            if not photo:
                message = bot.send_message(text=msg, parse_mode='HTML',
                                           disable_web_page_preview=False,
                                           chat_id=self.telegram_id,
                                           reply_markup=keyboard)
            else:
                message = bot.send_photo(chat_id=self.telegram_id, caption=msg,
                                         photo=photo, parse_mode='HTML', reply_markup=keyboard)
            if save_message_id:
                self.last_message_id = message.message_id
                self.save()
        except Exception as error:
            if "bot was blocked by the user" in str(error) or "user is deactivated" in str(
                    error) or "chat not found" in str(error):
                self.blocked = True
                self.save()

    def __str__(self):
        return self.telegram_id


class Post(models.Model):
    author = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    image_path = models.CharField(max_length=128, null=True)
    text = models.CharField(max_length=256, null=True)
    likes = models.IntegerField(default=0)
