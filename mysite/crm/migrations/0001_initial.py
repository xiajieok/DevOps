# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-23 13:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_type', models.CharField(choices=[('online', '网络班'), ('offline_weekend', '面授班（周末）'), ('offline_fulltime', '面授班（脱产）')], max_length=32, verbose_name='课程类型')),
                ('semster', models.IntegerField(verbose_name='学期')),
                ('star_date', models.DateField(verbose_name='开班日期')),
                ('gratute_date', models.DateField(blank=True, null=True, verbose_name='结业日期')),
            ],
            options={
                'verbose_name': '班级列表',
                'verbose_name_plural': '班级列表',
            },
        ),
        migrations.CreateModel(
            name='ConultRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(verbose_name='跟进内容...')),
                ('status', models.IntegerField(choices=[(1, '近期无报名计划'), (2, '1~2个月内报名'), (3, '1个月内报名'), (4, '已报名')], help_text='选择客户此时的状态', verbose_name='状态')),
                ('date', models.DateField(auto_now_add=True, verbose_name='跟进日期')),
            ],
            options={
                'verbose_name': '客户咨询跟进记录',
                'verbose_name_plural': '客户咨询跟进记录',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='课程名称')),
                ('price', models.IntegerField(verbose_name='面授价格')),
                ('online_price', models.IntegerField(verbose_name='网络班价格')),
                ('brief', models.TextField(verbose_name='课程简介')),
            ],
        ),
        migrations.CreateModel(
            name='CourseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_num', models.IntegerField(help_text='此处填写第几节课或第几天课程...必须为数字', verbose_name='节次')),
                ('date', models.DateField(auto_now_add=True, verbose_name='上课日期')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ClassList', verbose_name='班级（课程）')),
            ],
            options={
                'verbose_name': '上课记录',
                'verbose_name_plural': '上课记录',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qq', models.CharField(max_length=32, unique=True, verbose_name='QQ')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='姓名')),
                ('phone', models.BigIntegerField(blank=True, null=True, verbose_name='手机号')),
                ('stu_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='学号')),
                ('source', models.CharField(choices=[('QQ', 'QQ群'), ('referral', '内部转介绍'), ('51CTO', '51CTO'), ('agent', '招生代理'), ('others', '其他')], default='QQ', max_length=64, verbose_name='客户来源')),
                ('class_type', models.TextField(help_text='客户咨询的大概清空,客户个人信息备注等...', verbose_name='客户咨询内容详情')),
                ('status', models.CharField(choices=[('signed', '已报名'), ('unregistered', '未报名'), ('graduated', '已毕业')], default='unregistered', help_text='选择客户此时的状态', max_length=64, verbose_name='状态')),
                ('date', models.DateField(auto_now_add=True, verbose_name='咨询日期')),
                ('class_list', models.ManyToManyField(blank=True, to='crm.ClassList', verbose_name='已报班级')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='校区名称')),
                ('addr', models.CharField(max_length=128, verbose_name='地址')),
            ],
        ),
        migrations.CreateModel(
            name='StudyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.CharField(choices=[('checked', '已签到'), ('late', '迟到'), ('noshow', '缺勤'), ('leave_early', '早退')], default='checked', max_length=64, verbose_name='上课记录')),
                ('score', models.IntegerField(choices=[(100, 'A+'), (90, 'A'), (85, 'B+'), (80, 'B'), (70, 'B-'), (60, 'C+'), (0, 'D'), (-1, 'N/A'), (-100, 'COPY'), (-1000, 'FAIL')], default=-1, verbose_name='本节课成绩')),
                ('date', models.DateField(auto_now_add=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注')),
                ('course_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ConultRecord', verbose_name='第几天课程')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='学员')),
            ],
            options={
                'verbose_name': '学员学习纪录',
                'verbose_name_plural': '学员学习纪录',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='staffs',
            field=models.ManyToManyField(blank=True, to='crm.UserProfile'),
        ),
        migrations.AddField(
            model_name='customer',
            name='consulant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='课程顾问'),
        ),
        migrations.AddField(
            model_name='customer',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name='咨询课程'),
        ),
        migrations.AddField(
            model_name='customer',
            name='referral_from',
            field=models.ForeignKey(blank=True, help_text='若此客户是转介绍自内部学员,请在此处选择内部学员姓名', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='internal_referral', to='crm.Customer', verbose_name='转介绍自学员'),
        ),
        migrations.AddField(
            model_name='courserecord',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='讲师'),
        ),
        migrations.AddField(
            model_name='conultrecord',
            name='consulant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.UserProfile', verbose_name='跟踪人'),
        ),
        migrations.AddField(
            model_name='conultrecord',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Customer', verbose_name='所咨询客户'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='teachers',
            field=models.ManyToManyField(to='crm.UserProfile', verbose_name='讲师'),
        ),
        migrations.AlterUniqueTogether(
            name='studyrecord',
            unique_together=set([('course_record', 'student')]),
        ),
        migrations.AlterUniqueTogether(
            name='courserecord',
            unique_together=set([('course', 'day_num')]),
        ),
        migrations.AlterUniqueTogether(
            name='classlist',
            unique_together=set([('course', 'course_type', 'semster')]),
        ),
    ]
