# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-11 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_card_fine'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
