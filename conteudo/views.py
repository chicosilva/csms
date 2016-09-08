# coding=utf-8

from models import CodigoPromocional, New
from django.contrib import messages
import datetime
from forms import CodigoPromocionalForm, NoticiaForm, ImagemFormSet, Imagem
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from htmlmin.decorators import minified_response
import json
import socket

if socket.gethostname() == 's':
    URL_CLIENTE = ''
else:
    from keepsms.config.production_settings import URL_CLIENTE

@minified_response
def detalhes_noticia(request, id):

    noticia = New.objects.get(pk=id)

    if not noticia.access_number:
        noticia.access_number = 1
    else:
        noticia.access_number = noticia.access_number + 1

    noticia.save()

    dados = {
            'titulo': noticia.title,
            'imagens': Imagem.objects.filter(new=id),
            'noticia': noticia,
            'menu': "menu_conteudo",
    }

    return render(request, 'noticias/detalhes.html', dados)

def denuncia(request):
    from mensagem.api import enviar_denuncia
    enviar_denuncia(request.GET.get('noticia_id'))

    return HttpResponse(json.dumps({'sucesso': True}), content_type="application/json")

@login_required(login_url='/login/')
def nova_noticia(request):

    if request.method == 'POST':

        form = NoticiaForm(request.POST)

        if form.is_valid():

            noticia = form.save()

            noticia.url = "%s%s" % (URL_CLIENTE, reverse('conteudo:detalhes_noticia', kwargs={'id':noticia.pk}))
            noticia.save()

            diseaseInlineFormSet = ImagemFormSet(request.POST, request.FILES, instance=noticia)

            if diseaseInlineFormSet.is_valid():
                diseaseInlineFormSet.save()

            messages.success(request, u"Notícia cadastrada com sucesso!")
            return redirect(reverse('front:noticias'))

    else:
        form = NoticiaForm()
        imagens_formset = ImagemFormSet()

    dados = {
        'form': form,
        'formset': imagens_formset,
        'menu': "menu_conteudo",
        'titulo': u'Cadastrar Notícia',
    }

    return render(request, 'noticias/novo.html', dados)

@login_required(login_url='/login/')
def editar_noticia(request, id):

    noticia = New.objects.get(pk=id)

    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            messages.success(request, u'Notícia atualizado com sucesso!')

            noticia.url = "%s%s" % (URL_CLIENTE, reverse('conteudo:detalhes_noticia', kwargs={'id':noticia.pk}))
            noticia = form.save()

            diseaseInlineFormSet = ImagemFormSet(request.POST, request.FILES, instance=noticia)

            if diseaseInlineFormSet.is_valid():
                diseaseInlineFormSet.save()

            return redirect(reverse('front:noticias'))
    else:
        form = NoticiaForm(instance=noticia)
        imagens_formset = ImagemFormSet(instance=noticia)

    dados = {
            'titulo': u'Editar Notícia',
            'form': form,
            'formset': imagens_formset,
            'menu': "menu_conteudo",
            'noticia': noticia
    }

    return render(request, 'noticias/novo.html', dados)

@login_required(login_url='/login/')
def cancelar_noticia(request, id):

    noticia = New.objects.get(pk=id)

    if request.method == 'POST':
        New.objects.filter(id=id).update(data_cancelamento=datetime.datetime.now())
        messages.success(request, u'Registro removido com sucesso!')
        return redirect(reverse('front:noticias'))

    return render(request, 'noticias/cancelar.html', {'noticia': noticia, 'titulo': u'Remover Notícia', 'menu': "menu_conteudo",})

@login_required(login_url='/login/')
def novo_codigo(request):

    if request.method == 'POST':

        form = CodigoPromocionalForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request, u"Código cadastrado com sucesso!")
            return redirect(reverse('front:codigos_promocionais'))

    else:
        form = CodigoPromocionalForm()

    dados = {
        'form': form,
        'menu': "menu_conteudo",
        'titulo': u'Cadastrar Código Promocional',
    }

    return render(request, 'codigos/novo.html', dados)

@login_required(login_url='/login/')
def editar_codigo_promocional(request, id):

    codigo = CodigoPromocional.objects.get(pk=id)

    if request.method == 'POST':
        form = CodigoPromocionalForm(request.POST, instance=codigo)
        if form.is_valid():
            messages.success(request, u'Código promocional atualizado com sucesso!')
            form.save()
            return redirect(reverse('front:codigos_promocionais'))
    else:
        form = CodigoPromocionalForm(instance=codigo)

    return render(request, 'codigos/novo.html', {'titulo': u'Editar Código Promocional', 'form': form, 'menu': "menu_conteudo", 'codigo_promo': codigo})

@login_required(login_url='/login/')
def cancelar_codigo_promocional(request, id):

    codigo = CodigoPromocional.objects.get(pk=id)

    if request.method == 'POST':
        CodigoPromocional.objects.filter(id=id).update(data_cancelamento=datetime.datetime.now())
        messages.success(request, u'Registro removido com sucesso!')
        return redirect(reverse('front:codigos_promocionais'))

    return render(request, 'codigos/cancelar.html', {'codigo': codigo, 'menu': "menu_conteudo", 'titulo': u'Remover Código Promocional',})

def mapa(request):

    from autenticacao.models import Configuracao
    configuracao = Configuracao.objects.all().first()
    return render(request, 'noticias/mapa.html', {'titulo': u'Localização %s' % configuracao.nome,})

