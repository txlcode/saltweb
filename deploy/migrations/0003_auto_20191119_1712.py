# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-11-19 09:12
from __future__ import unicode_literals

import deploy.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0002_auto_20191119_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moduleattchment',
            name='attchment',
            field=models.FileField(blank=True, null=True, storage=deploy.storage.FileStorage(), upload_to='salt/module/HsYWX4NNrNGLvDEMrwpAmCN8Mry3wajhr3E8eAAHhDYCUkKyuffXhXsJexck3BAkU74yHTd6HnqfVwlQ', verbose_name='\u6a21\u5757\u4e0a\u4f20'),
        ),
    ]