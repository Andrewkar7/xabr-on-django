# Generated by Django 3.1 on 2021-02-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20210205_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='slug',
            field=models.SlugField(default='', max_length=70, verbose_name='URL'),
        ),
    ]