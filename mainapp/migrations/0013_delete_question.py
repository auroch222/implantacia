# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 10:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20160612_1347'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
