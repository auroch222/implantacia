# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0031_articlecontext_text5'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecontext',
            name='title4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]