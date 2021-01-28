# Generated by Django 3.1 on 2021-01-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210128_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
        migrations.AddField(
            model_name='post',
            name='like_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='кол-во'),
        ),
    ]
