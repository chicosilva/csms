# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import libs.util


class Migration(migrations.Migration):

    dependencies = [
        ('conteudo', '0004_auto_20150515_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='image',
            field=models.ImageField(upload_to=libs.util.upload_image, verbose_name='Imagem'),
        ),
    ]
