from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('django_flood/', include('tg_bot.urls')),
    path('admin/', admin.site.urls),
]

