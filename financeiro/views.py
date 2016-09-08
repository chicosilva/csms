# coding=utf-8

from models import Recarga, Credito, envia_email_recarga, ValorRecarga
from forms import FormConta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from libs.util import list_paginator, MESES
from pagseguro.api import PagSeguroItem, PagSeguroApi
import requests
from keepconfig.models import Cliente
import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from mensagem.models import Mensagem
import datetime
from django.contrib import messages
import socket

@login_required(login_url='/login/')
def tarifador(request):

    today = datetime.date.today()

    mes = request.GET.get('mes', today.month )

    mensages_cobradas, total_cobrado = 0, 0
    mensagens = Mensagem.objects.filter(data__month=mes)

    for mensagem in mensagens:
        if mensagem.valor:
                mensages_cobradas = mensages_cobradas + 1
                total_cobrado = total_cobrado + mensagem.valor
    dados = {
        'titulo': u'Tarifador',
        'mes': mes,
        'total_cobrado': total_cobrado,
        'mensages_cobradas': mensages_cobradas,
        'total': mensagens.count(),
        'meses': MESES,
        'mensagens': list_paginator(request, Mensagem.objects.filter(data__month=mes), 50),
        'menu': "menu_mensagens",
    }

    return render(request, 'recarga/tarifador.html', dados)

@login_required(login_url='/login/')
def recargas(request):

    dados = {
        'titulo': u'Recargas',
        'recargas': list_paginator(request, Recarga.objects.all(), 20),
        'menu': "menu_mensagens",
    }

    return render(request, 'recarga/recargas.html', dados)

@csrf_exempt
def recarga(request):

    url_recarga = 'http://piloto.site.com'

    if socket.gethostname() == 's':
        url_recarga = 'http://127.0.0.1:8008'

    if request.method == 'POST':

        form = FormConta(request.POST)

        if form.is_valid():

            recarga = form.save()
            return HttpResponseRedirect('/pagamento?recarga_id=%s&codigo_cliente=%s' % (recarga.pk, request.POST.get('codigo_cliente')))

    else:
        form = FormConta()

    dados = {
        'form': form,
        'menu': "menu_mensagens",
        'titulo': u'Recarga',
        'url_recarga': url_recarga,
        'valores': ValorRecarga.objects.all(),
    }

    return render(request, 'recarga/novo.html', dados)

def pagamento(request):

    codigo_cliente = request.GET.get('codigo_cliente')
    recarga_id     = request.GET.get('recarga_id')
    request.session['codigo_cliente'] = codigo_cliente

    recarga = Recarga.objects.get(pk=recarga_id)
    cliente = Cliente.objects.get(pk=codigo_cliente)

    item1 = PagSeguroItem(id=recarga.pk, description='Recarga Keep Mensagens - %s' % recarga.valor.valor, amount=recarga.valor.valor, quantity=1)
    pagseguro_api = PagSeguroApi(reference='%s-%s' % (codigo_cliente, recarga.pk), senderEmail=cliente.email, senderName=cliente.nome,)

    pagseguro_api.add_item(item1)
    data = pagseguro_api.checkout()

    if data['status_code'] != 200:
        recarga.data_cancelamento = datetime.datetime.now()
        recarga.save()
        messages.error(request, 'Ocorreu um erro para prosseguir a recarga, contate o suporte.')

        return HttpResponseRedirect('/recargas/' % cliente.url)

    requests.post("%s/cria-recarga-cliente/" % cliente.url, data={'recarga_id': recarga_id, 'valor_id': recarga.valor_id,'token': '92817488F00646D0$sso09asada'})

    dados = {
            'titulo': "Pagamento",
            'recarga': recarga,
            'cliente': cliente,
            'redirect_url': data['redirect_url'],
            'menu': "menu_mensagens",
    }

    return render(request, 'recarga/pagamento.html', dados)

def sucesso(request):
    return render(request, 'recarga/sucesso.html', {'titulo': u'Sucesso', 'cliente': Cliente.objects.get(pk=request.session['codigo_cliente'])})

@csrf_exempt
@require_http_methods(['POST'])
def criar_recarga_retorno(request):

    token = request.POST.get('token', False)
    recarga_id = request.POST.get('recarga_id',)
    valor_id = request.POST.get('valor_id',)

    if token == '92817488F00646D0$sso09asada':

        recarga = Recarga()
        recarga.valor_id = valor_id
        recarga.status_id = 1
        recarga.recarga_id = recarga_id
        recarga.save()

        return HttpResponse(json.dumps({'recarga_id': recarga_id}), content_type="application/json")

@csrf_exempt
@require_http_methods(['POST'])
def atualiza_credito(request):

    token = request.POST.get('token', False)
    recarga_id = request.POST.get('recarga_id', False)
    from keepconfig.models import KeepConfig

    if token == '92817488F00646D0$sso09asada':

        recarga = Recarga.objects.get(recarga_id=recarga_id)

        if recarga.status_id == 2:
            return HttpResponse(json.dumps({'ja_recarregado': True,}), content_type="application/json")

        credito = Credito.objects.first()
        credito.valor = credito.valor + recarga.valor.valor
        credito.save()

        recarga.status_id = 2
        recarga.save()

        config = KeepConfig.objects.all().first()
        config.valor_sms = recarga.valor.valor_sms
        config.save()

        envia_email_recarga(recarga)

        return HttpResponse(json.dumps({'recarga_id': recarga_id}), content_type="application/json")

    return HttpResponse(json.dumps({'erro': True}), content_type="application/json")