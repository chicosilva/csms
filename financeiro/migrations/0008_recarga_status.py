# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0007_auto_20150528_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='recarga',
            name='status',
            field=models.ForeignKey(default=1, verbose_name='Status', to='financeiro.StatusPagamento'),
        ),
    ]
