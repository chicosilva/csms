# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Cadastro')),
                ('data_cancelamento', models.DateTimeField(verbose_name='Cancelamento', null=True, editable=False, blank=True)),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Cadastro')),
                ('data_cancelamento', models.DateTimeField(verbose_name='Cancelamento', null=True, editable=False, blank=True)),
                ('nome', models.CharField(max_length=150, null=True, verbose_name='Nome', blank=True)),
                ('data_nascimento', models.DateField(null=True, verbose_name='Data de Nascimento', blank=True)),
                ('celular', models.CharField(unique=True, max_length=15, verbose_name='Celular')),
                ('cep', models.CharField(help_text=b'<a class="lbuscacep" target="_blank" href="http://www.buscacep.correios.com.br/servicos/dnec/menuAction.do?Metodo=menuEndereco">N\xc3\xa3o sabe o CEP? Consulte aqui!</a>', max_length=15, null=True, verbose_name='CEP', blank=True)),
                ('notificacoes', models.BooleanField(default=True, verbose_name='Receber Mensagens SMS/Voz?', editable=False)),
                ('origem', models.CharField(default=b'f', max_length=1, verbose_name='Origem', choices=[(b'f', 'Formul\xe1rio'), (b'p', 'Planilha'), (b't', 'Tablet'), (b'i', 'Indica\xe7\xe3o')])),
                ('numero_invalido', models.BooleanField(default=False, verbose_name='N\xfamero Inv\xe1lido?')),
                ('bairro', models.ForeignKey(verbose_name='Bairro', blank=True, to='localizacao.Bairro', null=True)),
                ('categoria', models.ForeignKey(verbose_name='Categoria', to='cadastro.Categoria')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
