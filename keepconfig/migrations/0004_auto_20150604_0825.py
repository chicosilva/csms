# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keepconfig', '0003_auto_20150601_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keepconfig',
            name='codigo_cliente',
            field=models.IntegerField(null=True, verbose_name='C\xf3digo do Cliente', blank=True),
        ),
    ]
