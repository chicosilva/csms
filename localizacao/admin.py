# coding=utf-8
from models import Bairro
from django.contrib import admin
from libs.util import cancelar, export_as_xls

class BairroAdmin(admin.ModelAdmin):

    list_display = ['nome', ]
    actions = [export_as_xls, cancelar]

    def has_delete_permission(self, request, obj=None): return False

    def get_actions(self, request):
        actions = super(BairroAdmin, self).get_actions(request)
        if actions.get('delete_selected'): del actions['delete_selected']

        return actions

admin.site.register(Bairro, BairroAdmin)
