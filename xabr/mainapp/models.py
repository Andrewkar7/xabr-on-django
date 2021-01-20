from django.db import models


# python manage.py migrate
# python manage.py makemigrations
# python manage.py migrate
# Создать суперпользователя через консоль: python manage.py createsuperuser / django / geekbrains


class Category(models.Model):
    name = models.CharField(verbose_name='название категории', max_length=64, default='new', unique=True)
    description = models.TextField(verbose_name='описание категории', blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название статьи', max_length=128)
    description = models.TextField(verbose_name='краткое описание статьи', blank=True)
    posts_text = models.TextField(verbose_name='текст статьи', blank=True)
    create_datetime = models.DateTimeField(verbose_name='дата создания', auto_now_add=True, blank=True)

    # при makemigrations необходимо указывать в [default: timezone.now] >>> timezone.now

    def __str__(self):
        return f"{self.name} ({self.category.name})"
