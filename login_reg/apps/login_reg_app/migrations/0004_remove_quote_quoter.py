# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-25 22:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0003_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='quoter',
        ),
    ]