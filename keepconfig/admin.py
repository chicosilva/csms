# coding=utf-8
from models import KeepConfig, Cliente
from django.contrib import admin

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'url', 'celular', 'id']


class KeepConfigAdmin(admin.ModelAdmin):
    list_display = ['codigo_cliente', 'valor_sms']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(KeepConfigAdmin, self).get_actions(request)
        if actions.get('delete_selected'): del actions['delete_selected']

        return actions

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(KeepConfig, KeepConfigAdmin)