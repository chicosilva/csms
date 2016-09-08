# coding:utf-8
from django.contrib import admin
from models import Recarga, Credito
from forms import FormConta
from libs.util import cancelar, export_as_xls

class ContaReceberAdmin(admin.ModelAdmin):
    form                = FormConta
    list_display        = ['data_cadastro', 'valor']
    actions             = [cancelar, export_as_xls]

    def save_model(self, request, obj, form, change):
        super(ContaReceberAdmin, self).save_model(request, obj, form, change)
        credito = Credito.objects.get(pk=1)
        credito.valor = credito.valor + obj.valor
        credito.save()

    def has_delete_permission(self, request, obj=None): return False

    def get_actions(self, request):
        actions = super(ContaReceberAdmin, self).get_actions(request)
        if actions.get('delete_selected'): del actions['delete_selected']

        return actions

class CreditoAdmin(admin.ModelAdmin):

    list_display        = ['valor_formatado',]

    def has_delete_permission(self, request, obj=None): return False

    def get_actions(self, request):
        actions = super(CreditoAdmin, self).get_actions(request)
        if actions.get('delete_selected'): del actions['delete_selected']

        return actions

    def has_add_permission(self, request): return False

    def has_delete_permission(self, request, obj=None): return False

    def get_actions(self, request):
        actions = super(CreditoAdmin, self).get_actions(request)
        if actions.get('delete_selected'): del actions['delete_selected']

        return actions

admin.site.register(Recarga, ContaReceberAdmin)
admin.site.register(Credito, CreditoAdmin)