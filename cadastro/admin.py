# coding=utf-8
from models import Usuario, Categoria
from django.contrib import admin
from libs.util import cancelar, export_as_xls

class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['nome', ]
    actions = [export_as_xls, cancelar]

    def has_delete_permission(self, request, obj=None): return False

    def get_actions(self, request):
        actions = super(CategoriaAdmin, self).get_actions(request)
        if actions.get('delete_selected'): del actions['delete_selected']

        return actions

class UsuarioAdmin(admin.ModelAdmin):

    list_display = ['nome', 'notificacoes', 'celular', 'bairro']
    search_fields = ['nome', 'email', 'celular']
    list_filter = ['notificacoes', 'categoria']
    actions = [export_as_xls, cancelar]

    def has_delete_permission(self, request, obj=None): return False

    def get_actions(self, request):
        actions = super(UsuarioAdmin, self).get_actions(request)
        if actions.get('delete_selected'): del actions['delete_selected']

        return actions

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Categoria, CategoriaAdmin)
