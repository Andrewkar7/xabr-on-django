# Generated by Django 3.1.5 on 2021-02-06 12:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0021_auto_20210206_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xabruser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 8, 12, 46, 30, 62262, tzinfo=utc)),
        ),
    ]
