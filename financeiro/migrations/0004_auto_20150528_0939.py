# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0003_recarga_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valorrecarga',
            name='data_cadastro',
        ),
        migrations.RemoveField(
            model_name='valorrecarga',
            name='data_cancelamento',
        ),
    ]
