# -*- coding: utf-8 -*-
from financeiro.models import Credito, saldo_positivo
from keepconfig.models import KeepConfig
from autenticacao.models import Configuracao

def informacoes_financeiras(request):

    credito = Credito.objects.all().first()
    sms = KeepConfig.objects.all().first()

    pode_atingir = 0
    if credito.valor > 0:
        pode_atingir = credito.valor / sms.valor_sms

    return {
        'total_credito': credito.valor_formatado(),
        'valor_sms': sms.valor_sms,
        'pode_atingir': '%.0f' % round(pode_atingir, 0),
        'saldo_positivo': saldo_positivo(),
        'codigo': sms.codigo_cliente,
        'configuracao': Configuracao.objects.all().first(),
        'is_mobile': request.user_agent.is_mobile,
    }