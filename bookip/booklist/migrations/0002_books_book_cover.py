# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-13 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='Book_cover',
            field=models.CharField(default='cover_not_available.jpg', max_length=1000),
        ),
    ]
