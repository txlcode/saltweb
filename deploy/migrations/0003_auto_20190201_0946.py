# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-01 01:46
from __future__ import unicode_literals

import deploy.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0002_auto_20190122_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moduleattchment',
            name='attchment',
            field=models.FileField(blank=True, null=True, storage=deploy.storage.FileStorage(), upload_to='salt/module/vHptR43jPjJnsPjlrbYcbXu3XHBUuqhxwXG6ClcYp7MkkUD9l3fnGVbJvsYCLkbxaSbL5Mcw37UNm4v7', verbose_name='\u6a21\u5757\u4e0a\u4f20'),
        ),
    ]
