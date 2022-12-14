# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-09-15 12:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0056_auto_20220915_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'd7ecd9c7-8f76-4206-922f-30fd03558364', max_length=128),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 15, 17, 45, 0, 767000)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'0ea6e3c3-17f2-4a1e-97c1-8af08c2075a7', max_length=512),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default=b'3513edd7-a1dc-471c-90e3-dd805851ce3e', max_length=1024),
        ),
    ]
