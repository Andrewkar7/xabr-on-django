import os
import json

from django.core.management.base import BaseCommand

from mainapp.models import Category, Post
from django.conf import settings
from authapp.models import XabrUser


def load_from_json(file_name):
    with open(os.path.join(settings.JSON_PATH, f'{file_name}.json'),
            encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        Category.objects.all().delete()
        [Category.objects.create(**category) for category in categories]

        posts = load_from_json('posts')
        Post.objects.all().delete()  # all() -> QuerySet -> .first() -> concrete object
        for post in posts:
            category_name = post['category']
            # Получаем категорию по имени
            # _category = Category.objects.get(name=category_name)
            # _category = Category.objects.filter(name=category_name).first()   # хороший способ
            # _category = list(Category.objects.filter(name=category_name))[0] - не самый лучший вариант
            _category = Category.objects.get(name=category_name)  # .get() -> concrete object возможно придется прописывать с try

            # Заменяем название категории объектом
            post['category'] = _category
            new_post = Post(**post)
            new_post.save()


        #if not len(ShopUser.objects.filter(username='django'))    # len лучше не использовать
        #if ShopUser.objects.filter(username='django').count() == 0:  # считает количество пользователей
        if not XabrUser.objects.filter(username='django').exists():
            #создаю суперпользователя
            XabrUser.objects.create_superuser(username='django', email='admin@xabr.local', password='geekbrains')