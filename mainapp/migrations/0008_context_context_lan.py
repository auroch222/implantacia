# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_context_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='context',
            name='context_lan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Language'),
        ),
    ]
