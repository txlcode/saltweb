# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-10-28 07:26
from __future__ import unicode_literals

import deploy.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0013_auto_20191028_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moduleattchment',
            name='attchment',
            field=models.FileField(blank=True, null=True, storage=deploy.storage.FileStorage(), upload_to='salt/module/CLEXYcLlsfJNhbdv9YhVa9XCSQd9Kq9vMruQLbMDdFEyTdWB3fBNJRQAkGtwr7Pw9VdVKPWb4U6myNUG', verbose_name='\u6a21\u5757\u4e0a\u4f20'),
        ),
    ]
