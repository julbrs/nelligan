# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_book_pickup'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='barcode',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
