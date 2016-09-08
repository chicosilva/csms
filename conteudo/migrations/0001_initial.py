# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import libs.util


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoPromocional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Cadastro')),
                ('data_cancelamento', models.DateTimeField(verbose_name='Cancelamento', null=True, editable=False, blank=True)),
                ('descricao', models.CharField(max_length=100, verbose_name='Descri\xe7\xe3o')),
                ('codigo', models.CharField(unique=True, max_length=10, verbose_name='C\xf3digo')),
                ('texto_codigo', models.TextField(max_length=100, verbose_name='Texto')),
                ('validade', models.DateField(verbose_name='Validade')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'C\xf3digo Promocional',
                'verbose_name_plural': 'C\xf3digos Promocionais',
            },
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Cadastro')),
                ('data_cancelamento', models.DateTimeField(verbose_name='Cancelamento', null=True, editable=False, blank=True)),
                ('title', models.CharField(max_length=70, null=True, verbose_name='Descri\xe7\xe3o', blank=True)),
                ('image', models.ImageField(upload_to=libs.util.upload_image, verbose_name='Imagem')),
                ('url', models.CharField(max_length=500, null=True, verbose_name='Link', blank=True)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Prancha',
                'verbose_name_plural': 'Pranchas',
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Cadastro')),
                ('data_cancelamento', models.DateTimeField(verbose_name='Cancelamento', null=True, editable=False, blank=True)),
                ('title', models.CharField(max_length=70, verbose_name='T\xedtulo')),
                ('texto', models.TextField(null=True, verbose_name='Texto', blank=True)),
                ('url', models.CharField(max_length=500, null=True, verbose_name='Link', blank=True)),
                ('slug', models.SlugField(max_length=255, null=True, blank=True)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Not\xedcia',
                'verbose_name_plural': 'Not\xedcias',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Cadastro')),
                ('data_cancelamento', models.DateTimeField(verbose_name='Cancelamento', null=True, editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='T\xedtulo')),
                ('video', models.TextField(verbose_name='Texto')),
                ('access_number', models.IntegerField(default=1, null=True, verbose_name='Acessos', blank=True)),
                ('slug', models.SlugField(max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'V\xeddeo',
                'verbose_name_plural': 'V\xeddeos',
            },
        ),
        migrations.AddField(
            model_name='imagem',
            name='new',
            field=models.ForeignKey(verbose_name='Usu\xe1rio', blank=True, to='conteudo.New', null=True),
        ),
    ]
