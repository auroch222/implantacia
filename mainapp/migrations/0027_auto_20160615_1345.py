# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0026_articlecontext_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlecontext',
            name='question_text',
        ),
        migrations.AddField(
            model_name='articlecontext',
            name='text1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='articlecontext',
            name='text2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='articlecontext',
            name='text3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='articlecontext',
            name='text4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='articlecontext',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='articlecontext',
            name='title2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='articlecontext',
            name='title3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
