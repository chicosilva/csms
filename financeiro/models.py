# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from libs.util import ModelDefault, moeda_brasileira_nosimbol
import locale
from pagseguro.signals import notificacao_recebida
import requests
import sendgrid
from keepsms.settings import SENDGRID_KEY
from django.template.loader import render_to_string
from django.template import Context


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class StatusPagamento(models.Model):
    class Meta:
        verbose_name = _(u'Status Pagamanto')
        verbose_name_plural = _(u'Status Pagamanto')

    descricao           = models.CharField(verbose_name=_(u'Descrição'), max_length=40,)
    def __unicode__(self): return self.descricao

class ValorRecarga(models.Model):
    class Meta:
        ordering = ['valor']
        verbose_name_plural = "Valor"

    valor_sms_inicio    = 0

    valor               = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True,)
    valor_sms           = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True,)

    def valor_formatado(self):return moeda_brasileira_nosimbol(self.valor)
    valor_formatado.short_description = u"Valor"
    def __unicode__(self): return "%s" % self.valor

    def total_envios(self):
        pode_atingir = self.valor / self.valor_sms
        return '%.0f' % round(pode_atingir, 0)

class Recarga(ModelDefault):
    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Recargas"

    valor               = models.ForeignKey(ValorRecarga, verbose_name=_(u'Valor'), default=1)
    status              = models.ForeignKey(StatusPagamento, verbose_name=_(u'Status'), default=1)
    data_pagamento      = models.DateField(null=True, blank=True, verbose_name=_(u'Data do Pagto'), editable=False)
    code                = models.CharField(verbose_name=_(u'Code'), max_length=555, editable=False, null=True, blank=True,)
    recarga_id          = models.IntegerField(verbose_name=_(u'Regarga Id'), null=True, blank=True)
    codigo_cliente      = models.IntegerField(verbose_name=_(u'Cód Cliente'), null=True, blank=True)

    def valor_formatado(self):return moeda_brasileira_nosimbol(self.valor)
    valor_formatado.short_description = u"Valor"

    def data_pagamento_formatada(self):
        if self.data_pagamento: return self.data_pagamento.strftime("%d/%m/%Y")
        return ''

    data_pagamento_formatada.short_description = u"Pgto"
    data_pagamento_formatada.admin_order_field = 'data_vencimento'

    def __unicode__(self): return self.valor.valor

class Credito(models.Model):
    class Meta:
        ordering = ['-id']
        verbose_name_plural = u"Créditos"

    valor               = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    def __unicode__(self): return "%s" % self.valor

    def valor_formatado(self):return moeda_brasileira_nosimbol(self.valor)
    valor_formatado.short_description = u"Valor"

def saldo_positivo():
    from keepconfig.models import KeepConfig

    credito = Credito.objects.all().first()
    sms = KeepConfig.objects.all().first()

    if credito.valor <= 0 or credito.valor < sms.valor_sms: return False

    return True

def envia_email_recarga(recarga):

    from autenticacao.models import Configuracao
    configuracao = Configuracao.objects.first()

    dados = {
        'recarga': recarga,
        'configuracao': configuracao,
    }

    html_content = render_to_string('recarga/email_recarga.html', Context(dados))
    sg = sendgrid.SendGridClient('user', SENDGRID_KEY)

    assunto = u"Keep Mensagens - Recarga efetuada com sucesso!"

    message = sendgrid.Mail(to=configuracao.email, subject=assunto, html=html_content, from_email='contato@s.com')
    sg.send(message)

def enviar_credito(codigo_cliente, recarga_id):

    from keepconfig.models import Cliente
    cliente = Cliente.objects.get(pk=codigo_cliente)

    requests.post("%s/atualiza-credito/" % cliente.url, data={'recarga_id': recarga_id, 'token': '92817488F00646D0$sso09asada'})

def load_signal(sender, transaction, **kwargs):

    status = transaction['status']
    reference = transaction['reference'].split('-')

    codigo_cliente = reference[0]
    recarga_id = reference[1]

    recarga = Recarga.objects.get(pk=recarga_id)
    recarga.code = transaction['code']

    if status == '3' or status == '4':

        enviar_credito(codigo_cliente, recarga_id)
        recarga.status_id = 2

    recarga.save()

notificacao_recebida.connect(load_signal)