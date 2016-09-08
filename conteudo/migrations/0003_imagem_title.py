# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0002_auto_20150515_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagem',
            name='title',
            field=models.CharField(max_length=70, null=True, verbose_name='Descri\xe7\xe3o', blank=True),
        ),
    ]
