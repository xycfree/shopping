# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-18 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodslist', '0002_auto_20170410_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uAddr',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uEmail',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uPassword',
            field=models.CharField(max_length=64),
        ),
    ]
