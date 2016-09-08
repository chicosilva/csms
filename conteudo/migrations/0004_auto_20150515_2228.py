# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0003_imagem_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='texto',
            field=models.TextField(null=True, verbose_name='Texto', blank=True),
        ),
    ]
