from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', verbose_name='avatar', blank=True, null=True)
    address = models.TextField(verbose_name='address', blank=True, null=True)
    phone = models.TextField(verbose_name='phone', blank=True, null=True)

    def get_avatar(self):
        return self.avatar.url if self.avatar else settings.STATIC_URL + 'images/default.png'
