# -*- coding: utf-8 -*-

from django import forms
from cadastro.models import Categoria, Usuario, celular_to_int

class ImportPlanilhaForm(forms.Form):
    arquivo = forms.FileField(label='Selelcione um arquivo .csv')
    categoria = forms.ChoiceField(label="Categora", choices=(), initial=1, widget=forms.Select(attrs={'class':'form-control'}))

    def __init__(self, *args, **kwargs):
        super(ImportPlanilhaForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].choices = [(pt.id, unicode(pt)) for pt in Categoria.objects.all()]
        self.fields['arquivo'].widget.attrs['class'] = 'form-control'
        self.fields['arquivo'].widget.attrs['required'] = True

    def clean_arquivo(self):
        file = "%s" % self.cleaned_data['arquivo']
        extension = file[-4:]
        if extension != '.csv': raise forms.ValidationError("O arquivo deve ser.csv")

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

    celular = forms.CharField(label="Categora", required=True)

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        for field in Usuario._meta.get_all_field_names():
            try:
                self.fields['%s' % field].widget.attrs['class'] = 'form-control'
            except:
                pass

    def clean_celular(self):

        if not celular_to_int(self.cleaned_data['celular']):
            raise forms.ValidationError(u"Formato Inválido.")

        return celular_to_int(self.cleaned_data['celular'])