# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-19 09:23
from __future__ import unicode_literals

import deploy.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0037_auto_20181219_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Models_fun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modules', models.CharField(db_index=True, max_length=50)),
                ('func', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='moduleattchment',
            name='attchment',
            field=models.FileField(blank=True, null=True, storage=deploy.storage.FileStorage(), upload_to='salt/module/hhkdD8vu3f7YEj44c6HbLYfMurWaHTTYNlSGgqTHUFppr7KC3XVdfS5EStYe4UVBXXBGrtvRWaWnv6KQ', verbose_name='\u6a21\u5757\u4e0a\u4f20'),
        ),
    ]
