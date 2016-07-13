# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=50, verbose_name='IP\u5730\u5740')),
                ('type', models.CharField(max_length=5, verbose_name='\u8fdc\u7a0b\u65b9\u5f0f', choices=[(b'W', b'Windows'), (b'V', b'VNC'), (b'R', b'Radmin'), (b'S1', b'Sehll'), (b'S2', b'Securecrt'), (b'P', b'putty')])),
                ('port', models.CharField(max_length=50, verbose_name='\u7aef\u53e3')),
                ('account', models.CharField(max_length=200, verbose_name='\u8d26\u53f7')),
                ('password', models.CharField(max_length=200, verbose_name='\u5bc6\u7801')),
                ('serverNO', models.CharField(max_length=200, verbose_name='\u8bbe\u5907\u7f16\u53f7')),
                ('system', models.CharField(max_length=200, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('time', models.CharField(max_length=50, verbose_name='\u8d2d\u7f6e\u65f6\u95f4')),
                ('purpose', models.CharField(max_length=50, verbose_name='\u7528\u9014')),
                ('remarks', models.CharField(max_length=50, verbose_name='\u5907\u6ce8')),
            ],
        ),
    ]
