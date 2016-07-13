# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_cabinetinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinetinfo',
            name='remarks',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5907\u6ce8'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='purpose',
            field=models.CharField(max_length=50, null=True, verbose_name='\u7528\u9014'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='remarks',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5907\u6ce8'),
        ),
        migrations.AlterField(
            model_name='serverinfo',
            name='serverNO',
            field=models.CharField(max_length=200, verbose_name='\u4e3b\u673a\u540d'),
        ),
    ]
