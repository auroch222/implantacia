# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0037_articlecontext_image7'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('title2', models.CharField(blank=True, max_length=200, null=True)),
                ('title3', models.CharField(blank=True, max_length=200, null=True)),
                ('text1', models.TextField(blank=True, null=True)),
                ('text2', models.TextField(blank=True, null=True)),
                ('text3', models.TextField(blank=True, null=True)),
                ('image1', models.FileField(blank=True, null=True, upload_to=b'')),
                ('image2', models.FileField(blank=True, null=True, upload_to=b'')),
                ('image3', models.FileField(blank=True, null=True, upload_to=b'')),
                ('image4', models.FileField(blank=True, null=True, upload_to=b'')),
                ('image5', models.FileField(blank=True, null=True, upload_to=b'')),
                ('image6', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
        ),
    ]
