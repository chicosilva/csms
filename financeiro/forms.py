# coding:utf-8
from models import Recarga, Credito
from django import forms

class FormConta(forms.ModelForm):
    class Meta:
        model = Recarga
        fields = "__all__"

class FormCredito(forms.ModelForm):
    class Meta:
        model = Credito
        fields = "__all__"

    valor = forms.CharField(label="Valor", required=True)