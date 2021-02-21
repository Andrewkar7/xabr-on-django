# Generated by Django 3.1 on 2021-02-16 17:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210216_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xabruser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 18, 17, 57, 16, 773962, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='xabruser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='xabruser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]