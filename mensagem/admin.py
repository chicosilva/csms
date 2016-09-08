# coding=utf-8
from models import Mensagem, MensagemPadrao

from django.contrib import admin
from libs.util import export_as_xls

class MensagemAdmin(admin.ModelAdmin):

    list_display            = ['usuario', 'data_pt', 'status_text']
    search_fields           = ['usuario__nome', 'texto']
    list_filter             = ['status',]
    actions                 = [export_as_xls]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(MensagemAdmin, self).get_actions(request)
        if actions.get('delete_selected'): del actions['delete_selected']

        return actions


class MensagemPadraoAdmin(admin.ModelAdmin):

    list_display            = ['texto',]
    search_fields           = ['texto',]
    actions                 = [export_as_xls]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(MensagemPadraoAdmin, self).get_actions(request)
        if actions.get('delete_selected'): del actions['delete_selected']

        return actions


admin.site.register(Mensagem, MensagemAdmin)
admin.site.register(MensagemPadrao, MensagemPadraoAdmin)