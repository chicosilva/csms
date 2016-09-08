# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Bairro',
                'verbose_name_plural': 'Bairros',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cep', models.CharField(unique=True, max_length=20, verbose_name='CEP')),
                ('bairro', models.CharField(max_length=255, null=True, verbose_name='Bairro', blank=True)),
                ('logradouro', models.CharField(max_length=255, null=True, verbose_name='logradouro', blank=True)),
                ('uf', models.CharField(max_length=15, null=True, verbose_name='UF', blank=True)),
                ('localidade', models.CharField(max_length=255, null=True, verbose_name='Localidade', blank=True)),
            ],
            options={
                'ordering': ['cep'],
                'verbose_name': 'Endere\xe7o',
                'verbose_name_plural': 'Endere\xe7os',
            },
        ),
    ]
