# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='colour',
            field=models.CharField(default='blue', max_length=50),
        ),
    ]
