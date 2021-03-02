# Generated by Django 3.1.5 on 2021-03-02 18:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_auto_20210225_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xabruser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 18, 6, 48, 24788, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='xabruser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
