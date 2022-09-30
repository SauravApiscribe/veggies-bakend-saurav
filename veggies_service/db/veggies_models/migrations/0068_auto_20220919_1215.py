# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-09-19 06:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0067_auto_20220919_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'5d7e2676-6263-4c57-8310-b6fd1269cd07', max_length=128),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 19, 12, 20, 40, 286000)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'4e04d317-20bf-47fd-840c-5f6c2ed1ba0e', max_length=512),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default=b'9bd1f7c8-4d68-4c6e-9203-064042c651f7', max_length=1024),
        ),
    ]