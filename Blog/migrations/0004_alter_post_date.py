# Generated by Django 4.0.4 on 2022-05-22 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
