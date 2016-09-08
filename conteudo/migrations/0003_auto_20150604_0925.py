# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensagem', '0008_auto_20150604_0925'),
        ('conteudo', '0002_auto_20150604_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagem',
            name='new',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.AddField(
            model_name='new',
            name='access_number',
            field=models.IntegerField(default=1, null=True, verbose_name='Tentativas', blank=True),
        ),
        migrations.AlterField(
            model_name='codigopromocional',
            name='data_cadastro',
            field=models.DateTimeField(verbose_name='Cadastro', null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='data_cadastro',
            field=models.DateTimeField(verbose_name='Cadastro', null=True, editable=False, blank=True),
        ),
        migrations.DeleteModel(
            name='Imagem',
        ),
    ]
