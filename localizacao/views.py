# coding=utf-8
from models import Endereco, get_endereco, endereco_json, Bairro
import json
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponse, redirect
from mensagem.forms import MensagemParticularForm
from django.contrib import messages
from mensagem.models import MensagemPadrao, Mensagem, data_agendamento
from cadastro.models import Usuario

@login_required(login_url='/login/')
def detalhes_bairro(request, id):

    bairro = Bairro.objects.get(pk=id)

    if request.method == 'POST':

            form = MensagemParticularForm(request.POST)

            if form.is_valid():

                dados_form = {
                    'data_agendamento': data_agendamento(request.POST.get('data_agendamento', False), request.POST.get('hora_envio', False)),
                    'mensagem_padrao_id': request.POST.get('mensagem_padrao', False),
                    'texto': request.POST.get('texto'),
                    'bairro_id': id,
                }

                for usuario in Usuario.objects.filter(bairro=id):

                    dados_form['usuario'] = usuario
                    Mensagem(**dados_form).save()

                messages.success(request, u"Mensagem enviada com sucesso, confira o status do envio no link mensagens")
                return redirect(reverse('localizacao:detalhes_bairro', kwargs={'id': id}))

    else:
        form = MensagemParticularForm()

    dados = {
        'bairro': bairro,
        'titulo': bairro,
        'form': form,
        'mensagens_padrao': MensagemPadrao.objects.all(),
        'mensagens': Mensagem.objects.filter(bairro=id)[:30],

    }

    return render(request, 'bairros/detalhes.html', dados)

def endereco(request):

    cep = request.GET.get('cep')

    try:
        endereco = Endereco.objects.get(cep=cep.replace('-', ''))
        return HttpResponse(json.dumps(endereco_json(endereco)), content_type="application/json")
    except:
        return HttpResponse(json.dumps(get_endereco(cep)), content_type="application/json")