# coding=utf-8
from django.conf.urls import patterns, url
urlpatterns = patterns('conteudo.views',

        url(r'^novo-codigo/$', 'novo_codigo', name='novo_codigo'),
        url(r'^cancelar-codigo-promocional/(?P<id>\d+)$', 'cancelar_codigo_promocional', name='cancelar_codigo_promocional'),
        url(r'^editar-codigo-promocional/(?P<id>\d+)$', 'editar_codigo_promocional', name='editar_codigo_promocional'),
        url(r'^nova-noticia/$', 'nova_noticia', name='nova_noticia'),
        url(r'^cancelar-noticia/(?P<id>\d+)$', 'cancelar_noticia', name='cancelar_noticia'),
        url(r'^editar-noticia/(?P<id>\d+)$', 'editar_noticia', name='editar_noticia'),
        url(r'^n/(?P<id>\d+)$', 'detalhes_noticia', name='detalhes_noticia'),
        url(r'^mapa/$', 'mapa', name='mapa'),
        url(r'^denuncia/$', 'denuncia', name='denuncia'),

)