# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-24 04:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0040_auto_20201023_2141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='address',
            new_name='addresses',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='veggies_models.Address'),
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'012cede6-e53e-46d2-bfa3-9cc14cafee13', max_length=128),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 24, 9, 46, 9, 202055)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'72e52b5d-8bc4-4c1b-9f2a-c67c117e1b9b', max_length=512),
        ),
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default=b'ef671cb0-b969-4372-9a20-705d7597646f', max_length=1024),
        ),
    ]
