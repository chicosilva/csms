# coding=utf-8
from os.path import join, dirname
from django.conf import settings

TEMPLATE_CONTEXT_PROCESSORS = settings.TEMPLATE_CONTEXT_PROCESSORS
STATICFILES_FINDERS = settings.STATICFILES_FINDERS
INSTALLED_APPS = settings.INSTALLED_APPS
STATIC_URL = settings.STATIC_URL
import socket

DOMINIO = 'http://localhost:8000'
NOME_SITE = u'Local Host'

if socket.gethostname() == 's':
    from local_settings import *
else:
    if socket.gethostname() != 's':
        from production_settings import *

        DOMINIO = URL_CLIENTE
        NOME_SITE = NOME_SITE_INSTALL

DEFAULT_FROM_EMAIL = u'{0}<naoresponda@{1}>'.format(NOME_SITE, DOMINIO)
EMAIL_HOST = 'smtp.s.com'
EMAIL_HOST_USER = 'contato@site.com'
EMAIL_HOST_PASSWORD = '2'
EMAIL_SUBJECT_PREFIX = u'[ %s ]' % NOME_SITE
EMAIL_PORT = 587
EMAIL_USE_TLS = True

RAIZ = dirname(dirname(__file__))
PUBLIC_ROOT = join(RAIZ, 'public')
MEDIA_ROOT = join(PUBLIC_ROOT, 'media')
STATIC_ROOT = join(PUBLIC_ROOT, 'static')
LOG_ROOT = join(PUBLIC_ROOT, 'logs')
TEMPLATE_DIRS = (join(RAIZ, 'templates'),)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
IMAGENS_EMAIL = ''

INSTALLED_APPS = ('suit',) + INSTALLED_APPS
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    "financeiro.processor.informacoes_financeiras",
)
SUIT_CONFIG = {
    'ADMIN_NAME': u'Administração %s' % NOME_SITE,
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': False,
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',
    'LIST_PER_PAGE': 50,

    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
    },
    'MENU': (

        {'app': 'cadastro', 'label': u'Gestão', 'icon': 'icon-cog', },

    ),
}

STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)
from apps import INSTALLED_APPS as IA

INSTALLED_APPS += IA
