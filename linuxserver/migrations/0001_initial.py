# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vendor', models.CharField(max_length=30, null=True)),
                ('sn', models.CharField(max_length=30, null=True)),
                ('product', models.CharField(max_length=30, null=True)),
                ('cpu_model', models.CharField(max_length=50, null=True)),
                ('cpu_num', models.CharField(max_length=2, null=True)),
                ('cpu_vendor', models.CharField(max_length=30, null=True)),
                ('memory_part_number', models.CharField(max_length=30, null=True)),
                ('memory_manufacturer', models.CharField(max_length=30, null=True)),
                ('memory_size', models.CharField(max_length=20, null=True)),
                ('device_model', models.CharField(max_length=30, null=True)),
                ('device_version', models.CharField(max_length=30, null=True)),
                ('device_sn', models.CharField(max_length=30, null=True)),
                ('device_size', models.CharField(max_length=30, null=True)),
                ('osver', models.CharField(max_length=30, null=True)),
                ('hostname', models.CharField(max_length=30, null=True)),
                ('os_release', models.CharField(max_length=30, null=True)),
                ('ipaddr', models.IPAddressField()),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668\u4fe1\u606f',
                'verbose_name_plural': '\u670d\u52a1\u5668\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('members', models.ManyToManyField(to='linuxserver.Host')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u4fe1\u606f',
                'verbose_name_plural': '\u4e3b\u673a\u4fe1\u606f',
            },
        ),
    ]
