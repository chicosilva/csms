# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20150604_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='data_cadastro',
            field=models.DateTimeField(verbose_name='Cadastro', null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='data_cadastro',
            field=models.DateTimeField(verbose_name='Cadastro', null=True, editable=False, blank=True),
        ),
    ]
