# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-23 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20160523_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyrecord',
            name='course_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.CourseRecord', verbose_name='第几天课程'),
        ),
    ]
