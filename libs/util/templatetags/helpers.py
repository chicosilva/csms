#coding:utf8
from django.utils.translation import gettext as _
from libs.util import codifica as _codifica
from libs.util.freegeoip import get_geodata
from django import template
import pprint, locale

register = template.Library()

@register.filter
def valor_parcela(value, arg):
    res = currency(float(value) / float(arg))
    res = res.replace('R$ ', '')
    return res.split(',')

@register.filter
def multiply(value, arg): return int(value) * int(arg)

@register.filter
def multiplyf(value, arg): return float(value) * float(arg)

@register.filter
def to_telefone(value):
    if len(value) < 11: return '(%s) %s-%s'%(value[0:2],value[2:6],value[6:10])
    else: return '(%s) %s-%s'%(value[0:2],value[2:7],value[7:11])

@register.filter
def to_cep(value):
    return '%s.%s-%s'%(value[0:2],value[2:5],value[5:8])

@register.filter
def sim_nao_boolean(value):
    return _(u'Yes') if value else _(u'No')

@register.filter
def somar(value, vlr): return float(value) + float(vlr)

@register.filter
def to_real(value):
    value = '%.2f'%float(value)
    return value.replace(',', '-').replace('.', ',').replace('-', '.')

@register.filter
def to_money(value):
     try: value = 'R$ {:20,.2f}'.format(float(value or 0))
     except: value = 'R$ {:20,.2f}'.format(value or 0)
     return value.replace(',', '-').replace('.', ',').replace('-', '.')

@register.filter
def float_to_real(value):
    value = '%.2f'%value
    return value.replace(',', '-').replace('.', ',').replace('-', '.')

@register.filter
def to_float(value):
    return float(value)

@register.filter
def to_flat_float(value):
     try: value = '{:0,.2f}'.format(float(value))
     except: value = '{:0,.2f}'.format(value)
     return value.replace(',', '').replace('.','')

@register.filter
def multiplica(value, mtp):
    return float(value) * float(mtp)

@register.filter
def default_if_zero(value, resp):
    if value == 0 or value == '0' or value == '0,00': return resp
    return value

@register.filter
def sum_percent(value, percent):
    return value + (value * percent / 100)

@register.filter
def codifica(value):
    return _codifica(value)

@register.filter
def split(value,sep):
    return value.split(sep)

@register.filter
def makerange(value, start):
    return [x for x in range(start, value + 1)]

@register.filter
def geo(value):
    try: return get_geodata(value)
    except: return None

@register.filter(name='currency')
def currency(value):
    try:
        locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
    except:
        locale.setlocale(locale.LC_ALL,'')
    loc = locale.localeconv()
    return locale.currency(value, loc['currency_symbol'], grouping=True)

@register.assignment_tag(takes_context=True)
def set_var(context, nome, valor, *args, **kwargs):
    context['%s'%nome] = valor
    return valor

@register.assignment_tag(takes_context=True)
def set_svar(context, nome, valor, *args, **kwargs):
    if not context['request'].session.get('tplvars'):
        context['request'].session.update({'tplvars': {}})
    context['request'].session['tplvars']['%s' % nome] = valor
    return valor

@register.filter
def link_externo(value):
    if 'http' in value:
        return True
    return False
