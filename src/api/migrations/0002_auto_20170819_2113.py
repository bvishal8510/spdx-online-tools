# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-19 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comparefileupload',
            name='message',
            field=models.CharField(default='old', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='convertfileupload',
            name='message',
            field=models.CharField(default='old', max_length=64),
            preserve_default=False,
        ),
    ]
