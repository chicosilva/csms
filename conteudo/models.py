# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from libs.util import ModelDefault, upload_image
from easy_thumbnails.files import get_thumbnailer

class New(ModelDefault):
    class Meta:
        verbose_name = _(u'Notícia')
        verbose_name_plural = _(u'Notícias')
        ordering = ['-id']

    title               = models.CharField(verbose_name=_(u'Título'), max_length=70)
    texto               = models.TextField(verbose_name=_(u'Texto'), blank=True, null=True)
    url                 = models.CharField(verbose_name=_(u'Link'), max_length=500, blank=True, null=True)
    slug                = models.SlugField(max_length=255, null=True, blank=True)
    access_number       = models.IntegerField(verbose_name=_(u'Cliques'), default=0, null=True, blank=True)

    def __unicode__(self): return u'%s' % self.title

class Imagem(ModelDefault):
    class Meta:
        verbose_name = _(u'Prancha')
        verbose_name_plural = _(u'Pranchas')
        ordering = ['-id']

    title               = models.CharField(verbose_name=_(u'Descrição'), max_length=70, blank=True, null=True)
    new                 = models.ForeignKey(New, verbose_name=_(u'Usuário'), blank=True, null=True)
    image               = models.ImageField(verbose_name=_(u'Imagem'), upload_to=upload_image,)

    def __unicode__(self): return u'%s' % self.title

    def get_full_imagem(self):
        return get_thumbnailer(self.image).get_thumbnail({'size': (500, 500), 'crop': True}).url

    def imagem(self):
        thumb_url = get_thumbnailer(self.image).get_thumbnail({'size': (160, 95), 'crop': True}).url
        return "<img src='%s'>" % thumb_url
    imagem.allow_tags = True

class CodigoPromocional(ModelDefault):
    class Meta:
        verbose_name = _(u'Código Promocional')
        verbose_name_plural = _(u'Códigos Promocionais')
        ordering = ['-id']

    descricao           = models.CharField(verbose_name=_(u'Descrição'), max_length=100,)
    codigo              = models.CharField(verbose_name=_(u'Código'), max_length=10, unique=True)
    texto_codigo        = models.TextField(verbose_name=_(u'Texto'), max_length=100,)
    validade            = models.DateField(verbose_name=_(u'Validade'),)

    def __unicode__(self): return u'%s' % self.descricao

    def save(self, *args, **kwargs):
        self.codigo = self.codigo.upper()
        super(CodigoPromocional, self).save(*args, **kwargs)