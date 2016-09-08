# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models

class Cliente(models.Model):
    class Meta:
        verbose_name = _(u'Cliente')
        verbose_name_plural = _(u'Clientes')
        ordering = ['nome']

    nome                = models.CharField(verbose_name=_(u'Nome'), max_length=150,)
    url                 = models.CharField(verbose_name=_(u'Url'), max_length=250,)
    celular             = models.CharField(verbose_name=_(u'Celular'), max_length=15, blank=True, null=True,)
    cep                 = models.CharField(verbose_name=_(u'CEP'), max_length=15, blank=True, null=True,)
    endereco            = models.CharField(verbose_name=_(u'Endereço'), max_length=250,  blank=True, null=True,)
    numero              = models.CharField(verbose_name=_(u'Número'), max_length=15, blank=True, null=True,)
    email               = models.EmailField(_('E-mail'), max_length=254, blank=True, null=True,)

    def __unicode__(self): return u'%s' % (self.nome)

class KeepConfig(models.Model):
    class Meta:
        verbose_name = _(u'Keep Config')
        verbose_name_plural = _(u'Configs')

    codigo_cliente      = models.IntegerField(verbose_name=_(u'Código do Cliente'), blank=True, null=True,)
    valor_sms           = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,)
    vendedor            = models.CharField(verbose_name=_(u'Nome'), max_length=254, blank=True, null=True,)
    email_vendedor      = models.EmailField(_('E-mail'), max_length=254, blank=True, null=True,)

    def __unicode__(self): return u'%s' % self.codigo_cliente