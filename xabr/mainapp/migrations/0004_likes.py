# Generated by Django 3.1 on 2021-02-02 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0003_auto_20210202_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='', max_length=70, verbose_name='URL')),
                ('text', models.TextField(verbose_name='комментировать')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата добавления')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.post', verbose_name='пост')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'лайк',
                'verbose_name_plural': 'лайки',
            },
        ),
    ]
