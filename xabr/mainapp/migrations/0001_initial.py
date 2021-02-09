# Generated by Django 3.1 on 2021-02-04 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64, unique=True, verbose_name='название категории')),
                ('slug', models.SlugField(max_length=70, verbose_name='URL')),
                ('description', models.TextField(blank=True, verbose_name='описание категории')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='название статьи')),
                ('slug', models.SlugField(max_length=70, verbose_name='URL')),
                ('description', models.TextField(blank=True, verbose_name='краткое описание статьи')),
                ('posts_text', models.TextField(blank=True, verbose_name='текст статьи')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('like_quantity', models.PositiveIntegerField(default=0, verbose_name='кол-во')),
                ('is_active', models.BooleanField(default=True, verbose_name='активна')),
                ('comment', models.TextField(blank=True, verbose_name='комментарии')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='', max_length=70, verbose_name='URL')),
                ('text', models.TextField(verbose_name='комментировать')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата добавления')),
                ('moderation', models.BooleanField(default=False, verbose_name='модерация')),
                ('email', models.EmailField(max_length=254)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.post', verbose_name='пост')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
            },
        ),
    ]
