# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20160610_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('title2', models.CharField(max_length=254)),
                ('text', models.TextField()),
                ('text2', models.TextField()),
                ('images', models.FileField(upload_to=b'')),
                ('menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Menu')),
                ('submenu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.SubMenu')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
    ]
