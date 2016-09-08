# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0016_recarga_codigo_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='valorrecarga',
            name='valor_sms',
            field=models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True),
        ),
    ]
