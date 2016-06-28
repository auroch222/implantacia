# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20160610_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submenu',
            name='order',
        ),
        migrations.AlterField(
            model_name='submenu',
            name='link_url',
            field=models.CharField(blank=True, help_text='URL or URI to the content, eg /about/ or http://foo.com/', max_length=100),
        ),
    ]