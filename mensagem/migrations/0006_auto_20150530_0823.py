# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensagem', '0005_auto_20150529_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensagem',
            name='status',
            field=models.ForeignKey(default=42, editable=False, to='mensagem.StatusMensagem', verbose_name='Status Mensagem'),
        ),
        migrations.AlterField(
            model_name='mensagem',
            name='texto',
            field=models.TextField(max_length=149, verbose_name='Texto'),
        ),
    ]
