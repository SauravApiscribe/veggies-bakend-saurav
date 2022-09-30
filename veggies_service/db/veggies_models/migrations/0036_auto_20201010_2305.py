# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-10 17:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veggies_models', '0035_auto_20201010_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(null=True)),
                ('used_points', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('products', models.ManyToManyField(to='veggies_models.OrderItem')),
            ],
        ),
        migrations.AlterField(
            model_name='login',
            name='token',
            field=models.CharField(default=b'19ece685-05ea-4e50-a6f3-67806fbbed42', max_length=128),
        ),
        migrations.AlterField(
            model_name='otp',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 10, 23, 10, 29, 662458)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uuId',
            field=models.CharField(default=b'2be75fda-cdb1-4b0d-baa9-a2617bdbf346', max_length=512),
        ),
        migrations.AddField(
            model_name='basket',
            name='default_delivery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='veggies_models.DefaultDelivery'),
        ),
    ]
