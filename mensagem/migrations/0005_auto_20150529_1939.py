# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensagem', '0004_remove_mensagem_status_http'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensagem',
            name='url',
        ),
        migrations.AddField(
            model_name='mensagem',
            name='enviar_link',
            field=models.BooleanField(default=False, verbose_name='Enviar Link de confirma\xe7\xe3o?'),
        ),
        migrations.AddField(
            model_name='mensagem',
            name='resposta',
            field=models.TextField(max_length=250, null=True, verbose_name='Resposta', blank=True),
        ),
    ]
