# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keepconfig', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('url', models.CharField(max_length=250, verbose_name='Url')),
                ('celular', models.CharField(max_length=15, verbose_name='Celular')),
                ('cep', models.CharField(max_length=15, null=True, verbose_name='CEP', blank=True)),
                ('endereco', models.CharField(max_length=250, verbose_name='Endere\xe7o')),
                ('numero', models.CharField(max_length=150, verbose_name='N\xfamero')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.RemoveField(
            model_name='keepconfig',
            name='ativo',
        ),
    ]
