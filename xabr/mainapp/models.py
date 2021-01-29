from django.db import models
from django.urls import reverse


# python manage.py migrate
# python manage.py migrate --run-syncdb
# python manage.py makemigrations
# python manage.py migrate
# Создать суперпользователя через консоль: python manage.py createsuperuser / django / geekbrains


class Category(models.Model):
    name = models.CharField(verbose_name='название категории', max_length=64, default='', unique=True)
    slug = models.SlugField(verbose_name='URL', max_length=70)
    description = models.TextField(verbose_name='описание категории', blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название статьи', max_length=128)
    slug = models.SlugField(verbose_name='URL', max_length=70)
    description = models.TextField(verbose_name='краткое описание статьи', blank=True)
    posts_text = models.TextField(verbose_name='текст статьи', blank=True)
    create_datetime = models.DateTimeField(verbose_name='дата создания', auto_now_add=True, blank=True)
    like_quantity = models.PositiveIntegerField('кол-во', default=0)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    # при makemigrations необходимо указывать в [default: timezone.now] >>> timezone.now

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    def get_absolute_url(self):  # Тут мы создали новый метод
        return reverse('blogapp:post_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
