# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20160621_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='cabinetInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cabinet', models.CharField(max_length=50, verbose_name='\u673a\u67dc')),
                ('ip', models.CharField(max_length=50, verbose_name='IP\u5730\u5740')),
                ('ip1', models.CharField(max_length=50, verbose_name='\u5185\u7f51IP')),
                ('asset', models.CharField(max_length=100, verbose_name='\u8d44\u4ea7\u53f7')),
                ('time', models.CharField(max_length=50, verbose_name='\u8d2d\u7f6e\u65f6\u95f4')),
                ('Warranty', models.CharField(max_length=5, verbose_name='\u662f\u5426\u8fc7\u4fdd', choices=[(b'Y', b'\xe6\x98\xaf'), (b'N', b'\xe5\x90\xa6')])),
                ('remarks', models.CharField(max_length=50, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u673a\u67dc\u4fe1\u606f',
                'verbose_name_plural': '\u673a\u67dc\u4fe1\u606f',
            },
        ),
    ]
