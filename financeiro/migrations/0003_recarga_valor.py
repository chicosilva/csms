# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0002_auto_20150528_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='recarga',
            name='valor',
            field=models.ForeignKey(default=1, verbose_name='Valor', to='financeiro.ValorRecarga'),
        ),
    ]
