# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-09-20 10:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0071_auto_20220920_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'eb6bdc0e-6da8-4e4b-aedb-6de5ee44be06', max_length=128),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 20, 16, 22, 1, 705000)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'3bb2f8d7-44fd-4fa1-ba19-e90cb69f0459', max_length=512),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default=b'1ffb333e-aa41-4893-82d4-d95395f17476', max_length=1024),
        ),
    ]
