# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-09-13 14:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0054_auto_20201107_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'5ad28fdb-5d53-49a8-b91b-c8a380f57dc0', max_length=128),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliveries',
            field=models.ManyToManyField(to='veggies_models.Delivery'),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 19, 47, 1, 812000)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'43ad152b-b3d0-4d4a-bf0c-3865c2d05fa4', max_length=512),
        ),
        migrations.AlterField(
            model_name='user',
            name='addresses',
            field=models.ManyToManyField(to='veggies_models.Address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default=b'3d08b57d-8cb2-43fc-80b7-e80ef399b158', max_length=1024),
        ),
    ]
