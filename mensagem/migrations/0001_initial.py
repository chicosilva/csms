# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0001_initial'),
        ('cadastro', '0001_initial'),
        ('conteudo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilaMensagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Cadastro')),
                ('data_cancelamento', models.DateTimeField(verbose_name='Cancelamento', null=True, editable=False, blank=True)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'FilaMensagem',
                'verbose_name_plural': 'FilaMensagem',
            },
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Cadastro')),
                ('data_cancelamento', models.DateTimeField(verbose_name='Cancelamento', null=True, editable=False, blank=True)),
                ('texto', models.TextField(max_length=150, verbose_name='Texto')),
                ('status_http', models.CharField(verbose_name='Status http', max_length=250, null=True, editable=False, blank=True)),
                ('destino', models.CharField(max_length=30, verbose_name='Destino', blank=True)),
                ('texto_resposta', models.CharField(verbose_name='Resposta', max_length=100, null=True, editable=False, blank=True)),
                ('valor', models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)),
                ('tipo_destino', models.CharField(verbose_name='Tipo destino', max_length=30, editable=False)),
                ('tipo_acao', models.CharField(verbose_name='Outgoing API?', max_length=30, editable=False)),
                ('tentativas', models.IntegerField(default=0, null=True, verbose_name='Tentativas', blank=True)),
                ('clicada', models.BooleanField(default=False, verbose_name='Clicada?')),
                ('particular', models.BooleanField(default=False, verbose_name='Mensagem particular?', editable=False)),
                ('data_agendamento', models.DateTimeField(null=True, verbose_name='Data de Agendamento', blank=True)),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data de envio')),
                ('url', models.CharField(max_length=500, null=True, verbose_name='Link', blank=True)),
                ('status_text', models.TextField(max_length=150, null=True, verbose_name='Texto Status', blank=True)),
                ('bairro', models.ForeignKey(verbose_name='Bairro', blank=True, to='localizacao.Bairro', null=True)),
                ('categoria', models.ForeignKey(verbose_name='Categoria', blank=True, to='cadastro.Categoria', null=True)),
                ('codigo_promocional', models.ForeignKey(verbose_name='Mensagem Padr\xe3o', blank=True, to='conteudo.CodigoPromocional', null=True)),
                ('imagem', models.ForeignKey(verbose_name='Imagem', blank=True, to='conteudo.Imagem', null=True)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Mensagem',
                'verbose_name_plural': 'Mensagens',
            },
        ),
        migrations.CreateModel(
            name='MensagemPadrao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Cadastro')),
                ('data_cancelamento', models.DateTimeField(verbose_name='Cancelamento', null=True, editable=False, blank=True)),
                ('nome', models.CharField(max_length=150, verbose_name='T\xedtulo')),
                ('texto', models.TextField(max_length=255, verbose_name='Texto')),
            ],
            options={
                'ordering': ['-pk'],
                'verbose_name': 'Mensagem Padr\xe3o',
                'verbose_name_plural': 'Mensagens Padr\xe3o',
            },
        ),
        migrations.CreateModel(
            name='StatusMensagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(verbose_name='Status', max_length=25, editable=False)),
                ('descricao', models.CharField(verbose_name='Descri\xe7\xe3o', max_length=250, editable=False)),
                ('consultar_api', models.BooleanField(default=False, verbose_name='Permitir consulta na APi?')),
                ('tarifar', models.BooleanField(default=False, verbose_name='Tarifar?')),
            ],
            options={
                'ordering': ['-pk'],
                'verbose_name': 'Mensagem',
                'verbose_name_plural': 'Mensagens',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=25, verbose_name='Status')),
            ],
            options={
                'ordering': ['-nome'],
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipo',
            },
        ),
        migrations.AddField(
            model_name='mensagem',
            name='mensagem_padrao',
            field=models.ForeignKey(blank=True, editable=False, to='mensagem.MensagemPadrao', null=True, verbose_name='Mensagem Padr\xe3o'),
        ),
        migrations.AddField(
            model_name='mensagem',
            name='noticia',
            field=models.ForeignKey(verbose_name='Not\xedcia', blank=True, to='conteudo.New', null=True),
        ),
        migrations.AddField(
            model_name='mensagem',
            name='status',
            field=models.ForeignKey(blank=True, editable=False, to='mensagem.StatusMensagem', null=True, verbose_name='Status Mensagem'),
        ),
        migrations.AddField(
            model_name='mensagem',
            name='tipo',
            field=models.ForeignKey(verbose_name='Tipo Mensagem', to='mensagem.Tipo'),
        ),
        migrations.AddField(
            model_name='mensagem',
            name='usuario',
            field=models.ForeignKey(editable=False, to='cadastro.Usuario', verbose_name='Usu\xe1rio'),
        ),
        migrations.AddField(
            model_name='filamensagem',
            name='mensagem',
            field=models.ForeignKey(verbose_name='Mensagem', to='mensagem.Mensagem'),
        ),
    ]
