# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.safestring import mark_safe
from libs.util import ModelDefault
import csv
import re
import os
from localizacao.models import Bairro

ORIGEM_FORMULARIO = 'f'
ORIGEM_PLANILHA = 'p'
ORIGEM_TABLET = 't'
ORIGEM_INDICACAO = 'i'

ORIGEM_CHOICES = (
            (ORIGEM_FORMULARIO, _(u'Formulário')),
            (ORIGEM_PLANILHA, _(u'Planilha')),
            (ORIGEM_TABLET, _(u'Tablet')),
            (ORIGEM_INDICACAO, _(u'Indicação')),
)

class Categoria(ModelDefault):
    class Meta:
        verbose_name = _(u'Categoria')
        verbose_name_plural = _(u'Categorias')
        ordering = ['nome']

    nome                = models.CharField(verbose_name=_(u'Nome'), max_length=150)
    def __unicode__(self): return u'%s' % self.nome

    def total_clientes(self): return Usuario.objects.filter(categoria=self.pk).count()


class Operadora(ModelDefault):
    class Meta:
        verbose_name = _(u'Operadora')
        verbose_name_plural = _(u'Operadoras')
        ordering = ['nome']

    nome                = models.CharField(verbose_name=_(u'Nome'), max_length=150)
    def __unicode__(self): return u'%s' % self.nome

class Usuario(ModelDefault):
    class Meta:
        verbose_name = _(u'Cliente')
        verbose_name_plural = _(u'Clientes')
        ordering = ['nome']

    operadora           = models.ForeignKey(Operadora, verbose_name=_(u'Operadora'), blank=True, null=True,)
    bairro              = models.ForeignKey(Bairro, verbose_name=_(u'Bairro'), blank=True, null=True,)
    categoria           = models.ForeignKey(Categoria, verbose_name=_(u'Categoria'),)
    nome                = models.CharField(verbose_name=_(u'Nome'), max_length=150, blank=True, null=True,)
    data_nascimento     = models.DateField(verbose_name=_(u'Data de Nascimento'), auto_now_add=False, blank=True, null=True)
    celular             = models.CharField(verbose_name=_(u'Celular'), max_length=15, unique=True)
    cep                 = models.CharField(verbose_name=_(u'CEP'), max_length=15, blank=True, null=True, help_text=mark_safe('<a class="lbuscacep" target="_blank" href="http://www.buscacep.correios.com.br/servicos/dnec/menuAction.do?Metodo=menuEndereco">Não sabe o CEP? Consulte aqui!</a>'))
    notificacoes        = models.BooleanField(verbose_name=_(u'Receber Mensagens SMS/Voz?'), default=True, blank=True, editable=False)
    origem              = models.CharField(u"Origem", max_length=1, default=ORIGEM_FORMULARIO, choices=ORIGEM_CHOICES,)
    numero_invalido     = models.BooleanField(verbose_name=_(u'Número Inválido?'), default=False, blank=True, )

    def __unicode__(self):
        if not self.nome: return u"Cliente 00%s" % self.pk
        return u'%s' % (self.nome)

    def celular_tostr(self):

        if len(self.celular) >= 11: return '(%s) %s - %s' %(self.celular[0:2], self.celular[2:7], self.celular[7:11])
        return '(%s) %s - %s' %(self.celular[0:2], self.celular[2:6], self.celular[6:11])

def celular_to_int(numero):

    celular = re.sub('[()-]', '', numero)
    celular = celular.replace(" ", "")

    if int(celular[:1]) == 0:
        celular = celular[1:]

    if len(celular) < 9:
        return False

    if len(celular) > 11:
        return False

    ddds = range(11,99)
    ddd = int(celular[:2])

    if not ddd in ddds:
        return False

    return celular

def importa_arquivo_csv(arquivo, categoria):
    with open(arquivo, 'r') as f:
        reader = csv.reader(f)
        total_importacoes = 0

        for row in reader:

            celular, cep, nome = "", "", ""

            try: cep = row[1]
            except IndexError: pass

            try:nome = row[2]
            except IndexError:pass

            try:
                celular = celular_to_int(row[0])
                if not Usuario.objects.filter(celular=celular).exists() and celular:
                    Usuario(celular=celular, cep=cep, nome=nome, categoria_id=categoria).save()
                    total_importacoes = total_importacoes + 1
            except: pass

    if os.path.exists(arquivo):os.remove(arquivo)
    return total_importacoes