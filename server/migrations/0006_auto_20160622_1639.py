# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_auto_20160622_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverinfo',
            name='serverNO',
            field=models.CharField(max_length=200, null=True, verbose_name='\u4e3b\u673a\u540d'),
        ),
    ]
