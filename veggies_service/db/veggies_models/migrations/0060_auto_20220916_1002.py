# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-09-16 04:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0059_auto_20220915_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'22588cce-ce6f-4bcb-a31c-26fa58ffee93', max_length=128),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 16, 10, 7, 4, 793000)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'55f22cde-cb26-4260-a08a-be668f54f63f', max_length=512),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default=b'324cf63d-7240-4e63-b1ea-c3186184c519', max_length=1024),
        ),
    ]
