# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import libs.util


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0003_auto_20150604_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_cadastro', models.DateTimeField(verbose_name='Cadastro', null=True, editable=False, blank=True)),
                ('data_cancelamento', models.DateTimeField(verbose_name='Cancelamento', null=True, editable=False, blank=True)),
                ('title', models.CharField(max_length=70, null=True, verbose_name='Descri\xe7\xe3o', blank=True)),
                ('image', models.ImageField(upload_to=libs.util.upload_image, verbose_name='Imagem')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Prancha',
                'verbose_name_plural': 'Pranchas',
            },
        ),
        migrations.AlterField(
            model_name='new',
            name='access_number',
            field=models.IntegerField(default=0, null=True, verbose_name='Cliques', blank=True),
        ),
        migrations.AddField(
            model_name='imagem',
            name='new',
            field=models.ForeignKey(verbose_name='Usu\xe1rio', blank=True, to='conteudo.New', null=True),
        ),
    ]
