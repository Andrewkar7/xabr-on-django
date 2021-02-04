from datetime import timedelta

from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.timezone import now

from xabr import settings


def get_activation_key_express():
    return now() + timedelta(hours=48)




class XabrUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)
    aboutMe = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(	default=(now() + timedelta(hours=48)))
    like_quantity = models.PositiveIntegerField('кол-во', default=0)


    def is_activation_key_expired(self):
        return now() > self.activation_key_expires

    def send_verify_mail(self):
        verify_link = reverse(
            'auth:verify',
            kwargs={
                'email': self.email,
                'activation_key': self.activation_key
            },
        )
        title = f'Подтверждение учетной записи {self.username}'
        message = f'Для подтверждения учетной записи {self.username} на портале ' \
                  f'{settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'

        return send_mail(title, message, settings.EMAIL_HOST_USER, [self.email], fail_silently=False)
