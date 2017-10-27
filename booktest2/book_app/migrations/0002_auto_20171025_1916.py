# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gcontent', tinymce.models.HTMLField()),
            ],
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hcomment',
            field=models.CharField(max_length=200, verbose_name='功夫'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hgender',
            field=models.BooleanField(default=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hname',
            field=models.CharField(max_length=20, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='isDelete',
            field=models.BooleanField(default=False, verbose_name='状态'),
        ),
    ]
