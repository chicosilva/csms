# coding=utf-8
from django.conf.urls import patterns, url
urlpatterns = patterns('localizacao.views',
        url(r'^get-endereco/$', 'endereco', name='endereco'),
        url(r'^detalhes-bairro/(?P<id>\d+)$', 'detalhes_bairro', name='detalhes_bairro'),
)