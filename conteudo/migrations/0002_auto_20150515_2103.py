# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='access_number',
        ),
        migrations.AddField(
            model_name='new',
            name='id_url',
            field=models.CharField(max_length=255, null=True, verbose_name='ID Url', blank=True),
        ),
        migrations.AddField(
            model_name='new',
            name='url',
            field=models.CharField(max_length=255, null=True, verbose_name='Link', blank=True),
        ),
    ]
