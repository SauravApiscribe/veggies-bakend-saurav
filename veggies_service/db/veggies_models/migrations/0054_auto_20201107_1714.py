# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-07 11:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0053_auto_20201106_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='slot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slot_for_deliveries', to='veggies_models.Slot'),
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'93dcd2ca-6141-422c-ab6d-0619030b0855', max_length=128),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 7, 17, 19, 12, 714201)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'26589b45-2ea8-4dc3-919c-dda60a7891a2', max_length=512),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default=b'9469d5d1-d763-4c86-a101-5a0573f09e28', max_length=1024),
        ),
    ]
