# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_auto_20160622_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinetinfo',
            name='remarks',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
    ]
