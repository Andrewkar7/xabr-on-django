import re
import transliterate
from django.db import models
from django.urls import reverse
from authapp.models import XabrUser
from django.db.models.signals import pre_save
from django.utils.text import slugify
from unidecode import unidecode
from django.template import defaultfilters
import random
import string

MD = 'MD'
STATUS_CHOICES = (
    ('True', 'is_active'),
    ('MD', 'on_moderation'),
    ('False', 'not_is_active'),
)

MD = 'MD'
STATUS_CHOICES = (
    ('True', 'Опубликована'),
    ('MD', 'На модерации'),
    ('False', 'Черновик'),
)


class Category(models.Model):
    """класс категории поста"""
    name = models.CharField(verbose_name='название категории', max_length=64, default='', unique=True)
    slug = models.SlugField(verbose_name='уникальный адрес', max_length=70)
    description = models.TextField(verbose_name='описание категории', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Post(models.Model):
    """класс поста"""

    user = models.ForeignKey(XabrUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название статьи', max_length=128)
    slug = models.SlugField(verbose_name='уникальный адрес', max_length=70, unique=True)
    description = models.TextField(verbose_name='краткое описание статьи', blank=True)
    posts_text = models.TextField(verbose_name='текст статьи', blank=True)
    create_datetime = models.DateTimeField(verbose_name='дата создания', auto_now_add=True, blank=True)
    like_quantity = models.PositiveIntegerField('кол-во', default=0)
    is_active = models.CharField(verbose_name='статус', max_length=128, choices=STATUS_CHOICES)
    comment = models.TextField(verbose_name='комментарии', blank=True)

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = ('-create_datetime',)

    def __str__(self):
        return f"{self.name} ({self.category.name} {self.is_active})"

    def get_absolute_url(self):
        return reverse('blogapp:post_list')


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug = defaultfilters.slugify(unidecode(instance.name))
    slugs = Post.objects.filter()
    for slug_old in slugs.values("slug"):
        if slug in slug_old["slug"]:
            instance.slug = "%s-%s" % (slug, random_string_generator(size=4))
            break
        else:
            instance.slug = slug


pre_save.connect(pre_save_post_receiver, sender=Post)


class Comments(models.Model):
    """класс комментариев к постам"""
    user = models.ForeignKey(XabrUser, verbose_name="пользователь", related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="пост", on_delete=models.CASCADE)
    text = models.TextField("комментировать")
    created = models.DateTimeField("дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField("модерация", default=False)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"
        ordering = ('-created',)

    def __str__(self):
        return f"{self.user}"


class Like(models.Model):
    user = models.ForeignKey(XabrUser, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='URL', max_length=70, default='')
    is_active = models.BooleanField(verbose_name='активна', default=True)

    class Meta:
        verbose_name = "лайк"
        verbose_name_plural = "лайки"
