# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-31 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='vote',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]