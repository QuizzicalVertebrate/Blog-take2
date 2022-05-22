# Generated by Django 4.0.4 on 2022-05-22 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Body',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='post',
            name='Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]