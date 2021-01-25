from django.db import models
from django.contrib.auth.models import User

#если захотим сделать свою модель, придется снести старую бд
#class XabrUser(AbstractUser):
    #age = models.PositiveSmallIntegerField(verbose_name='возраст', null=True)
    #gender = models.CharField('пол', blank=True, max_length=10)
    #avatar = models.ImageField(upload_to='users_avatars', blank=True)