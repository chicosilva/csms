# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0013_auto_20150604_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recarga',
            name='data_cadastro',
            field=models.DateTimeField(verbose_name='Cadastro', null=True, editable=False, blank=True),
        ),
    ]
