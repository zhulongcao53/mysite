# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipadd', models.IPAddressField(verbose_name='IP\u5730\u5740')),
                ('time', models.CharField(max_length=50, verbose_name='\u65f6\u95f4')),
                ('cpu', models.CharField(max_length=255, verbose_name='CPU%', blank=True)),
                ('cpu_detail', models.CharField(max_length=255, verbose_name='CPU\u8be6\u60c5', blank=True)),
                ('mem', models.CharField(max_length=255, verbose_name='\u5185\u5b58%', blank=True)),
                ('mem_detail', models.CharField(max_length=255, verbose_name='\u5185\u5b58\u8be6\u60c5', blank=True)),
                ('disk', models.CharField(max_length=255, verbose_name='\u78c1\u76d8%', blank=True)),
                ('disk_detail', models.CharField(max_length=255, verbose_name='\u78c1\u76d8\u8be6\u60c5', blank=True)),
                ('net', models.CharField(max_length=255, verbose_name='\u6d41\u91cf bytes/s', blank=True)),
                ('net_detail', models.CharField(max_length=1000, verbose_name='\u6d41\u91cf\u8be6\u60c5', blank=True)),
                ('tcp', models.CharField(max_length=255, verbose_name='tcp\u8fde\u63a5\u72b6\u6001', blank=True)),
                ('process_down', models.CharField(max_length=255, verbose_name='DOWN-\u8fdb\u7a0b', blank=True)),
                ('process_alived', models.CharField(max_length=255, verbose_name='Process_UP', blank=True)),
            ],
        ),
    ]
