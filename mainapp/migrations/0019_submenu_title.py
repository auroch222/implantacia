# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_auto_20160613_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='submenu',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]