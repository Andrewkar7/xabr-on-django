# Generated by Django 3.1.5 on 2021-01-20 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210120_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posts_text',
            field=models.TextField(blank=True, verbose_name='текст статьи'),
        ),
    ]
