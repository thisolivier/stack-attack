# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 08:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_portal', '0002_auto_20170901_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator]),
        ),
    ]
