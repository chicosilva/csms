# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensagem', '0007_auto_20150604_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensagem',
            name='imagem',
        ),
        migrations.AlterField(
            model_name='filamensagem',
            name='data_cadastro',
            field=models.DateTimeField(verbose_name='Cadastro', null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='mensagem',
            name='data_cadastro',
            field=models.DateTimeField(verbose_name='Cadastro', null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='mensagempadrao',
            name='data_cadastro',
            field=models.DateTimeField(verbose_name='Cadastro', null=True, editable=False, blank=True),
        ),
    ]
