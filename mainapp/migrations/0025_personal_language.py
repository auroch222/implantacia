# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_auto_20160614_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='Language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Language'),
        ),
    ]