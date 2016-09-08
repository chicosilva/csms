# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0015_recarga_recarga_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='recarga',
            name='codigo_cliente',
            field=models.IntegerField(null=True, verbose_name='C\xf3d Cliente', blank=True),
        ),
    ]
