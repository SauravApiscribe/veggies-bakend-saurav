# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-02 01:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0024_auto_20201001_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='used_points',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'6e5e9e76-92ec-4fc4-97f5-7f9bdc29e36c', max_length=128),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 1, 51, 53, 979342)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'b9158160-6a0c-45ba-9b6e-8e65428e7456', max_length=512),
        ),
    ]
