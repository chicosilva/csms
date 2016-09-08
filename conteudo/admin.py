# coding=utf-8
from models import New
from django.contrib import admin

class NewAdmin(admin.ModelAdmin):

    exclude             = ("slug",)
    list_display        = ['title','data_pt']
    search_fields       = ['title',]

admin.site.register(New, NewAdmin)
