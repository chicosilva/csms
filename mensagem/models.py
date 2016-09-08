# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from libs.util import ModelDefault
from cadastro.models import Usuario, Categoria
import datetime
from localizacao.models import Bairro
from conteudo.models import CodigoPromocional, New
from django.db.models.signals import post_save

class MensagemPadrao(ModelDefault):
    class Meta:
        verbose_name = _(u'Mensagem Padrão')
        verbose_name_plural = _(u'Mensagens Padrão')
        ordering = ['-pk']

    nome                = models.CharField(verbose_name=_(u'Título'), max_length=150, )
    texto               = models.TextField(verbose_name=_(u'Texto'), max_length=255,)
    def __unicode__(self): return u'%s' % self.texto

class StatusMensagem(models.Model):
    class Meta:
        verbose_name = _(u'Mensagem')
        verbose_name_plural = _(u'Mensagens')
        ordering = ['-pk']

    codigo              = models.CharField(verbose_name=_(u'Status'), max_length=25, editable=False)
    descricao           = models.CharField(verbose_name=_(u'Descrição'), max_length=250, editable=False)
    consultar_api       = models.BooleanField(verbose_name=_(u'Permitir consulta na APi?'), default=False, blank=True, )
    tarifar             = models.BooleanField(verbose_name=_(u'Tarifar?'), default=False, blank=True, )

    def __unicode__(self): return u'%s' % self.descricao

    def style(self):
        codigos = {'120': 'success', '999': 'danger', '015': 'danger'}
        try:
            return codigos[self.codigo]
        except:
            return "label"

class Tipo(models.Model):
    class Meta:
        verbose_name = _(u'Tipo')
        verbose_name_plural = _(u'Tipo')
        ordering = ['-nome']

    nome              = models.CharField(verbose_name=_(u'Status'), max_length=25,)
    def __unicode__(self): return u'%s' % self.nome

class Mensagem(ModelDefault):
    class Meta:
        verbose_name = _(u'Mensagem')
        verbose_name_plural = _(u'Mensagens')
        ordering = ['-id']

    tipo                = models.ForeignKey(Tipo, verbose_name=_(u'Tipo Mensagem'), blank=False, null=False,)
    status              = models.ForeignKey(StatusMensagem, verbose_name=_(u'Status Mensagem'), editable=False, default=42)
    mensagem_padrao     = models.ForeignKey(MensagemPadrao, verbose_name=_(u'Mensagem Padrão'), blank=True, null=True, editable=False)
    codigo_promocional  = models.ForeignKey(CodigoPromocional, verbose_name=_(u'Mensagem Padrão'), blank=True, null=True)
    noticia             = models.ForeignKey(New, verbose_name=_(u'Notícia'), blank=True, null=True)
    usuario             = models.ForeignKey(Usuario, verbose_name=_(u'Usuário'), editable=False)
    bairro              = models.ForeignKey(Bairro, verbose_name=_(u'Bairro'), blank=True, null=True,)
    categoria           = models.ForeignKey(Categoria, verbose_name=_(u'Categoria'), blank=True, null=True, )
    texto               = models.TextField(verbose_name=_(u'Texto'), max_length=149,)
    resposta            = models.TextField(verbose_name=_(u'Resposta'), max_length=250,  blank=True, null=True,)
    enviar_link         = models.BooleanField(verbose_name=_(u'Enviar Link de confirmação?'), default=False, blank=True,)
    destino             = models.CharField(verbose_name=_(u'Destino'), max_length=30, blank=True, null=False)
    texto_resposta      = models.CharField(verbose_name=_(u'Resposta'), max_length=100, blank=True, null=True, editable=False)
    valor               = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True,)
    tipo_destino        = models.CharField(verbose_name=_(u'Tipo destino'), max_length=30, editable=False)
    tipo_acao           = models.CharField(verbose_name=_(u'Outgoing API?'), max_length=30, editable=False)
    tentativas          = models.IntegerField(verbose_name=_(u'Tentativas'), default=0, null=True, blank=True)
    clicada             = models.BooleanField(verbose_name=_(u'Clicada?'), default=False, blank=True, )
    particular          = models.BooleanField(verbose_name=_(u'Mensagem particular?'), default=False, blank=True, editable=False )
    data_agendamento    = models.DateTimeField(verbose_name=_(u'Data de Agendamento'), blank=True, null=True)
    data                = models.DateField(verbose_name=_(u'Data de envio'), auto_now_add=True)
    status_text         = models.TextField(verbose_name=_(u'Texto Status'), max_length=150, blank=True, null=True)

    def __unicode__(self): return u'%s' % self.campanha

    def atualiza_status(self):

        from mensagem.api import consulta_sms
        consulta_sms(self)
        return ''

    def save(self, *args, **kwargs):
        self.destino = self.usuario.celular
        super(Mensagem, self).save(*args, **kwargs)

    def fonte(self):

        fonte = ''

        if self.particular: fonte = u"Msg particular"
        if not self.bairro and not self.categoria and not self.particular: fonte = u"Para Todos"
        if self.bairro and self.categoria: fonte = u"B. %s e cat. %s" % (self.bairro, self.categoria)
        if self.bairro and not self.categoria: fonte = u"B. %s" % self.bairro
        if not self.bairro and self.categoria: fonte = u"Cat. %s" % self.categoria

        tipo = ''
        if self.codigo_promocional:tipo = U"Código Promocional"
        if self.noticia: tipo = u"Notícia"

        return "%s<br>%s" % (fonte, tipo)

    def celular_tostr(self):

        if len(self.destino) >= 11: return '(%s) %s - %s' %(self.destino[0:2], self.destino[2:7], self.destino[7:11])
        return '(%s) %s - %s' %(self.destino[0:2], self.destino[2:6], self.destino[6:11])

    def celular_tostr(self):

        if len(self.destino) >= 11: return '(%s) %s - %s' %(self.destino[0:2], self.destino[2:7], self.destino[7:11])
        return '(%s) %s - %s' %(self.destino[0:2], self.destino[2:6], self.destino[6:11])

class FilaMensagem(ModelDefault):
    class Meta:
        verbose_name = _(u'FilaMensagem')
        verbose_name_plural = _(u'FilaMensagem')
        ordering = ['-id']

    mensagem               = models.ForeignKey(Mensagem, verbose_name=_(u'Mensagem'),)

    def __unicode__(self): return u'%s' % self.mensagem

def data_agendamento(data_agendamento, hora_envio):

    if not data_agendamento: return None

    hora = "09:00"

    if data_agendamento:
        if hora_envio: hora = hora_envio
        data_agendamento = datetime.datetime.strptime("%s %s:00" % (data_agendamento, hora), '%d/%m/%Y %H:%M:%S')

    return data_agendamento

def reenviar_mensagem(id):

    mensagem = Mensagem.objects.get(pk=id)

    if not mensagem.data_agendamento:

        mensagem.pk = None
        mensagem.save()

    return mensagem

def enviar_para_fila(sender, instance, created, **kwargs):

    if created:
        FilaMensagem(mensagem=instance).save()

def save_envio_mensagem_conteudo(request, entity):

    dados_form = {
                'data_agendamento': data_agendamento(request.POST.get('data_agendamento', False), request.POST.get('hora_envio', False)),
                'texto': request.POST.get('texto'),
                'tipo_id': 2,
                'status_id': 40,
                'enviar_link': request.POST.get('enviar_link', False),
                "%s_id" % entity: request.POST.get('%s' % entity)
    }

    if request.POST.get('categoria', False): dados_form['categoria_id'] = request.POST.get('categoria')
    if request.POST.get('bairro', False): dados_form['bairro_id'] = request.POST.get('bairro')

    kwargs = {}
    if request.POST.get('categoria', False): kwargs['categoria'] = request.POST.get('categoria')
    if request.POST.get('bairro', False): kwargs['bairro'] = request.POST.get('bairro')

    usuarios = Usuario.objects.filter(**kwargs).filter(numero_invalido=False).filter(notificacoes=True)

    for usuario in usuarios:

            dados_form['usuario'] = usuario
            Mensagem(**dados_form).save()

    return True

post_save.connect(enviar_para_fila, sender=Mensagem, dispatch_uid="enviar_para_fila")