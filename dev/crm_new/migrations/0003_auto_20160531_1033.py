# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-31 10:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_new', '0002_auto_20160531_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='QQ',
            new_name='qq',
        ),
    ]
