# coding=utf-8
from dajaxice.decorators import dajaxice_register
from django.http import HttpResponse
from dajax.core import Dajax
# from cep import Correios
#
# @dajaxice_register
# def cep(request, cep, cepid):
#     cmps, campos = ['endereco', 'bairro', 'cidade', 'uf', 'numero'], {}
#     for campo in cmps: campos.update({campo: cepid.replace('cep', campo)})
#     correios, dajax = Correios(), Dajax()
#     endereco = correios.consulta(cep)
#     if endereco:
#         endereco = endereco[0]
#         print endereco
#         dajax.assign('#%s' % campos['cidade'], 'value', endereco['Localidade'])
#         dajax.assign('#%s' % campos['bairro'], 'value', endereco['Bairro'])
#         dajax.assign('#%s' % campos['endereco'], 'value', endereco['Logradouro'].split(' -')[0])
#         dajax.assign('#%s' % campos['uf'], 'value', endereco['UF'])
#         dajax.script('$("#%s").focus();' % campos['numero'])
#         dajax.script('$.unblockUI();')
#     return dajax.json()