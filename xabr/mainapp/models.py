from django.db import models


class XabrCategory(models.Model):
    name = models.CharField('название категории', max_length=64)
    description = models.TextField('описание категории', blank=True)
    #is_active = models.BooleanField(verbose_name='активна', default=True)



