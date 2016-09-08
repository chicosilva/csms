# coding:utf-8
from django.template.defaultfilters import slugify
import threading
from libs.util.decorators import threaded
from django.conf import settings
from django.db import models
from datetime import datetime
import decimal
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from pyExcelerator import *
from django.contrib.admin.util import lookup_field
from django.utils.html import strip_tags
from django.contrib import messages
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

EXPORT_RECORDS_LIMIT = 500
import locale
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.mail import EmailMultiAlternatives

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def list_paginator(request, list, number):
    paginator = Paginator(list, number)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        list = paginator.page(paginator.num_pages)

    return list


MESES = (
    ('01', _('Janeiro')),
    ('02', _('Fevereiro')),
    ('03', _(u'Março')),
    ('04', _('Abril')),
    ('05', _('Maio')),
    ('06', _('Junho')),
    ('07', _('Julho')),
    ('08', _('Agosto')),
    ('09', _('Setembro')),
    ('10', _('Outubro')),
    ('11', _('Novembro')),
    ('12', _('Dezembro')),
)


class MesListFilter(admin.SimpleListFilter):
    title = _(u'Mês')
    parameter_name = 'mes'

    def lookups(self, request, model_admin):
        return (
            ('01', _('Janeiro')),
            ('02', _('Fevereiro')),
            ('03', _(u'Março')),
            ('04', _('Abril')),
            ('05', _('Maio')),
            ('06', _('Junho')),
            ('07', _('Julho')),
            ('08', _('Agosto')),
            ('09', _('Setembro')),
            ('10', _('Outubro')),
            ('11', _('Novembro')),
            ('12', _('Dezembro')),
        )

    def queryset(self, request, queryset): return queryset


def export_as_xls(modeladmin, request, queryset):
    """
    Generic xls export admin action.
    """
    if queryset.count() > EXPORT_RECORDS_LIMIT:
        messages.error(request,
                       "Can't export more then %s Records in one go. Narrow down your criteria using filters or search" % str(
                           EXPORT_RECORDS_LIMIT))
        return HttpResponseRedirect(request.path_info)
    fields = []

    #PUT THE LIST OF FIELD NAMES YOU DON'T WANT TO EXPORT
    exclude_fields = []

    #foreign key related fields
    extras = ['']

    if not request.user.is_staff:
        raise PermissionDenied

    for f in modeladmin.list_display:
        if f not in exclude_fields:
            fields.append(f)
    fields.extend(extras)

    opts = modeladmin.model._meta

    wb = Workbook()
    ws0 = wb.add_sheet('0')
    col = 0
    field_names = []

    # write header row
    for field in fields:
        ws0.write(0, col, "%s" % field)
        field_names.append(field)
        col = col + 1
    row = 1

    # Write data rows
    for obj in queryset:
        col = 0
        for field in field_names:
            if field in extras:
                try:
                    val = [eval('obj.' + field)]  #eval sucks but easiest way to deal
                except:
                    val = ['']
            else:
                try:
                    val = lookup_field(field, obj, modeladmin)
                except:
                    val = ['']

            try:
                if not val[-1]:
                    ws0.write(row, col, "")
                else:
                    ws0.write(row, col, u"%s" % strip_tags(val[-1]).strip())
            except:
                if not val[-1]:
                    ws0.write(row, col, "--")
                else:
                    ws0.write(row, col, u"%s" % val[-1])

            col = col + 1

        row = row + 1

    wb.save('/tmp/output.xls')
    response = HttpResponse(open('/tmp/output.xls', 'r').read(), content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % unicode(opts).replace('.', '_')
    return response

export_as_xls.short_description = u"Exportar seleção para XLS"

def valida_campos_vazios(dados):
    for k, v in dados.items():
        if not v or v == "":
            return False

    return True

def handle_uploaded_file(f, file_dir):

    with open(file_dir, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_image(instance, filename):
    fname = slugify(filename[:-4])
    return '%s/%s.%s' % (instance.__class__.__name__.lower(), fname, filename.split('.')[-1])

def clean_valor_moeda(valor):
    if not valor or valor == "": return 0
    valor = valor.replace(".", "")
    valor = valor.replace(",", ".")
    return decimal.Decimal(valor)


def valor(obj):
    return moeda_brasileira(obj.valor)

class CustomManager(models.Manager):
    def get_queryset(self):
        return super(CustomManager, self).get_queryset().filter(data_cancelamento__isnull=True)


class RegistroCanceladoManager(models.Manager):
    def get_queryset(self):
        return super(RegistroCanceladoManager, self).get_queryset().filter(data_cancelamento__isnull=False)

class ModelDefault(models.Model):
    class Meta:         abstract = True

    data_cadastro       = models.DateTimeField(verbose_name=_(u'Cadastro'), editable=False, null=True, blank=True)
    data_cancelamento   = models.DateTimeField(verbose_name=_(u'Cancelamento'), editable=False, null=True, blank=True)

    objects = CustomManager()
    cancelados = RegistroCanceladoManager()

    def data_pt(self):
        return self.data_cadastro.strftime("%d/%m/%Y %H:%M")

    data_pt.short_description = "Cadastro"
    data_pt.admin_order_field = 'data_cadastro'

    def data_cancelamento_formatada(self):
        if self.data_cancelamento:
            return self.data_cancelamento.strftime("%d/%m/%Y %H:%M")
        return ''

    data_cancelamento_formatada.short_description = "Cancelamento"
    data_cancelamento_formatada.admin_order_field = 'data_cancelamento'

    def save(self, *args, **kwargs):
        self.data_cadastro = timezone.localtime(timezone.now())

        super(ModelDefault, self).save(*args, **kwargs)

def cancelar(modeladmin, request, queryset):
    messages.success(request, 'Registro(s) cancelado(s) com sucesso!')
    queryset.update(data_cancelamento=datetime.now())

cancelar.short_description = "Cancelar e Inutilizar Registro(s)"

BASE64_KEY = getattr(settings, 'BASE64_KEY', '87GalhT4a7l')
try:
    EMAIL_SENDER = settings.DEFAULT_FROM_EMAIL
except:
    EMAIL_SENDER = settings.EMAIL_HOST_USER

class EmailThread(threading.Thread):
    def __init__(self, subject, html, body, from_email, recipient_list, headers, bcc, fail_silently, ):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.html = html
        self.headers = headers
        self.bcc = bcc
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMultiAlternatives(subject=self.subject, body=self.body, from_email=self.from_email,
                                     to=self.recipient_list, bcc=self.bcc, headers=self.headers)
        if self.html: msg.attach_alternative(self.html, "text/html")
        msg.extra_headers.update(self.headers)
        msg.send(self.fail_silently)

def moeda_brasileira(numero):
    if not numero: numero = 0
    return locale.currency(numero)


def moeda_brasileira_nosimbol(numero):
    if not numero: numero = 0
    return locale.currency(numero, symbol=None)

def send_mail(subject, recipient_list, html, reply=None, body='', from_email=EMAIL_SENDER, bcc=None, headers=None,
              fail_silently=False, *args, **kwargs):
    if not headers: headers = {'Reply-To': ','.join(recipient_list)}
    if reply: headers = {'Reply-To': reply}
    EmailThread(subject, html, body, from_email, recipient_list, headers, bcc, fail_silently).start()