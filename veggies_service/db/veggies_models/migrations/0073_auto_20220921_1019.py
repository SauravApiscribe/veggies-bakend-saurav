# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-09-21 04:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0072_auto_20220920_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'79b55b37-cb96-44a1-9da7-ebca765ec407', max_length=128),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 21, 10, 24, 56, 425176)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'f906b3a1-6d61-47f4-86e3-2bb9412f4404', max_length=512),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default=b'3b35b74b-d3c3-400e-b0b3-e58d4d1f7e4a', max_length=1024),
        ),
    ]