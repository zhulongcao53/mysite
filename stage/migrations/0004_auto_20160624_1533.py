# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0003_auto_20160623_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicinfo',
            name='cpu_detail',
        ),
        migrations.RemoveField(
            model_name='basicinfo',
            name='disk_detail',
        ),
        migrations.RemoveField(
            model_name='basicinfo',
            name='mem_detail',
        ),
        migrations.RemoveField(
            model_name='basicinfo',
            name='net',
        ),
        migrations.RemoveField(
            model_name='basicinfo',
            name='net_detail',
        ),
        migrations.RemoveField(
            model_name='basicinfo',
            name='process_alived',
        ),
        migrations.RemoveField(
            model_name='basicinfo',
            name='process_down',
        ),
        migrations.RemoveField(
            model_name='basicinfo',
            name='tcp',
        ),
        migrations.RemoveField(
            model_name='basicinfo',
            name='time',
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='MAC',
            field=models.CharField(max_length=100, verbose_name='MAC', blank=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='sys_bit',
            field=models.CharField(max_length=100, verbose_name='32/64\u4f4d', blank=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='sys_version',
            field=models.CharField(max_length=255, verbose_name='\u64cd\u4f5c\u7cfb\u7edf', blank=True),
        ),
    ]
