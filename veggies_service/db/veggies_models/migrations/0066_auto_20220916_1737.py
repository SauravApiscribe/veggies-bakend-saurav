# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-09-16 12:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0065_auto_20220916_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'f09316bb-63f3-4b85-bbc3-d6279c53015f', max_length=128),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 16, 17, 42, 54, 112000)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'6bced2ab-17d2-4d61-a011-414ae91f32c4', max_length=512),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default=b'ace2c388-3bd5-416f-8e43-ad1aa1aee280', max_length=1024),
        ),
    ]