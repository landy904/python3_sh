# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('user_name', models.CharField(max_length=20, verbose_name='用户名')),
                ('user_pass', models.CharField(max_length=64, verbose_name='密码')),
                ('user_mail', models.CharField(max_length=30, verbose_name='邮箱')),
                ('user_active', models.BooleanField(default=False)),
                ('user_recv', models.CharField(max_length=30, verbose_name='收件人')),
                ('user_address', models.CharField(max_length=80, verbose_name='地址')),
                ('user_code', models.CharField(max_length=6, verbose_name='邮编')),
                ('user_tele', models.CharField(max_length=11, verbose_name='手机')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
