# Generated by Django 3.1.5 on 2021-03-02 18:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_auto_20210302_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xabruser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 18, 7, 2, 414066, tzinfo=utc)),
        ),
    ]
