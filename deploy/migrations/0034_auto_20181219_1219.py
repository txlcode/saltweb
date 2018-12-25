# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-19 04:19
from __future__ import unicode_literals

import deploy.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0033_auto_20181219_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moduleattchment',
            name='attchment',
            field=models.FileField(blank=True, null=True, storage=deploy.storage.FileStorage(), upload_to='salt/module/NnTLmtPvmtr4BgphvTVn8xh7rmQkYWM5Ytt589gAFnEJsfj6aM9tpkxvSgRagEHsMcSv74XDEbvRJPL5', verbose_name='\u6a21\u5757\u4e0a\u4f20'),
        ),
        migrations.AlterField(
            model_name='salt_event_returns',
            name='fun_args',
            field=models.CharField(max_length=255),
        ),
    ]
