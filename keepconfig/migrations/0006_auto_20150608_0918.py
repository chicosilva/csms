# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keepconfig', '0005_cliente_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='keepconfig',
            name='email_vendedor',
            field=models.EmailField(max_length=254, null=True, verbose_name='E-mail', blank=True),
        ),
        migrations.AddField(
            model_name='keepconfig',
            name='vendedor',
            field=models.CharField(max_length=254, null=True, verbose_name='Nome', blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='E-mail', blank=True),
        ),
    ]
