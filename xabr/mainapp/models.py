from django.db import models
from django.urls import reverse
from authapp.models import XabrUser


class Category(models.Model):
    """класс категории поста"""
    name = models.CharField(verbose_name='название категории', max_length=64, default='', unique=True)
    slug = models.SlugField(verbose_name='URL', max_length=70)
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
    slug = models.SlugField(verbose_name='URL', max_length=70, unique=True)
    description = models.TextField(verbose_name='краткое описание статьи', blank=True)
    posts_text = models.TextField(verbose_name='текст статьи', blank=True)
    create_datetime = models.DateTimeField(verbose_name='дата создания', auto_now_add=True, blank=True)
    like_quantity = models.PositiveIntegerField('кол-во', default=0)
    is_active = models.BooleanField(verbose_name='активна', default=False)
    comment = models.TextField(verbose_name='комментарии', blank=True)

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    def get_absolute_url(self):
        return reverse('blogapp:post_detail', args=[str(self.id)])


class Comments(models.Model):
    """класс комментариев к постам"""
    user = models.ForeignKey(XabrUser, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="пост", on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='URL', max_length=70, default='')
    text = models.TextField("комментировать")
    created = models.DateTimeField("дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField("модерация", default=False)
    email = models.EmailField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"
        ordering = ('created',)

    def __str__(self):
        return "{}".format(self.user)


class Like(models.Model):
    user = models.ForeignKey(XabrUser, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='URL', max_length=70, default='')
    is_active = models.BooleanField(verbose_name='активна', default=True)

    class Meta:
        verbose_name = "лайк"
        verbose_name_plural = "лайки"
