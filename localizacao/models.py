# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
import requests

class Bairro(models.Model):
    class Meta:
        verbose_name = _(u'Bairro')
        verbose_name_plural = _(u'Bairros')
        ordering = ['nome']

    nome                = models.CharField(verbose_name=_(u'Nome'), max_length=150)
    def __unicode__(self): return u'%s' % self.nome

    def total_clientes(self):
        from cadastro.models import Usuario
        return Usuario.objects.filter(bairro=self.pk).count()

class Endereco(models.Model):
    class Meta:
        verbose_name = _(u'Endereço')
        verbose_name_plural = _(u'Endereços')
        ordering = ['cep']

    cep                   = models.CharField(verbose_name=_(u'CEP'), max_length=20, unique=True)
    bairro                = models.CharField(verbose_name=_(u'Bairro'), max_length=255, blank=True, null=True,)
    logradouro            = models.CharField(verbose_name=_(u'logradouro'), max_length=255, blank=True, null=True,)
    uf                    = models.CharField(verbose_name=_(u'UF'), max_length=15, blank=True, null=True,)
    localidade            = models.CharField(verbose_name=_(u'Localidade'), max_length=255, blank=True, null=True,)

    def __unicode__(self): return u'%s' % (self.bairro)

def endereco_json(obj):
    if not obj: return {}

    bairro = add_bairro(obj.bairro)

    dados = {'cep': obj.cep, 'bairro_id': False, 'bairro': obj.bairro, 'logradouro': obj.logradouro, 'uf': obj.uf,'localidade': obj.localidade,}

    if bairro: dados['bairro_id'] = bairro.pk

    return dados

def add_bairro(nome):

    if not nome: return False

    if not Bairro.objects.filter(nome=nome).exists():
        bairro = Bairro(nome=nome)
        bairro.save()
        return bairro
    else:
        return Bairro.objects.get(nome=nome)

def get_endereco(cep):

    cep = cep.replace('-','')

    try:
        result = requests.get('http://cep.correiocontrol.com.br/%s.json' % cep)
        r = result.json()

        if not Endereco.objects.filter(cep=cep).exists():
            endereco = Endereco(cep=r['cep'], bairro=r['bairro'], logradouro=r['logradouro'], uf=r['uf'], localidade=r['localidade'])
            endereco.save()
            return endereco_json(endereco)

        return endereco_json(Endereco.objects.get(cep=cep))
    except:return {}

def buscar_cep():

    for cep in range(38700001, 38706900):

        if not Endereco.objects.filter(cep=cep).exists():
            try:
                r = get_endereco(cep)
                Endereco(cep=r['cep'], bairro=r['bairro'], logradouro=r['logradouro'], uf=r['uf'], localidade=r['localidade']).save()
            except:
                pass