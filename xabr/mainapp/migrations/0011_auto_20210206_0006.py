# Generated by Django 3.1 on 2021-02-05 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_like_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='created',
        ),
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
    ]