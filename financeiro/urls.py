# coding=utf-8
from django.conf.urls import patterns, url
urlpatterns = patterns('financeiro.views',
    url(r'^nova-recarga/$', 'recarga', name='recarga'),
    url(r'^recargas/$', 'recargas', name='recargas'),
    url(r'^tarifador/$', 'tarifador', name='tarifador'),
    url(r'^pagamento/sucesso/$', 'sucesso', name='sucesso'),
    url(r'^atualiza-credito/$', 'atualiza_credito', name='atualiza_credito'),
    url(r'^pagamento/$', 'pagamento', name='pagamento'),
    url(r'^cria-recarga-cliente/$', 'criar_recarga_retorno', name='criar_recarga_retorno'),

)