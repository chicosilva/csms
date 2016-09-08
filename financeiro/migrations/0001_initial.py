# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name_plural': 'Cr\xe9ditos',
            },
        ),
        migrations.CreateModel(
            name='Recarga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Cadastro')),
                ('data_cancelamento', models.DateTimeField(verbose_name='Cancelamento', null=True, editable=False, blank=True)),
                ('descricao', models.CharField(max_length=200, verbose_name='Descri\xe7\xe3o')),
                ('status', models.CharField(verbose_name='Status', max_length=20, null=True, editable=False, blank=True)),
                ('valor', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('data_pagamento', models.DateField(verbose_name='Data do Pagto', null=True, editable=False, blank=True)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name_plural': 'Recargas',
            },
        ),
    ]
