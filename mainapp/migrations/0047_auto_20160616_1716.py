# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0046_auto_20160616_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='submenu',
            name='data2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='submenu',
            name='data3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='submenu',
            name='image1',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='submenu',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='submenu',
            name='image3',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='submenu',
            name='image4',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='submenu',
            name='image5',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='submenu',
            name='image6',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='submenu',
            name='image7',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='submenu',
            name='title2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='submenu',
            name='title3',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
