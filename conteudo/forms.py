# -*- coding: utf-8 -*-
from models import CodigoPromocional, New, Imagem
from django import forms
from django.forms.models import inlineformset_factory

class CodigoPromocionalForm(forms.ModelForm):
    class Meta:
        model = CodigoPromocional
        fields = "__all__"

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = New
        fields = "__all__"

class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = "__all__"

ImagemFormSet = inlineformset_factory(New, Imagem, extra=5, form=NoticiaForm)