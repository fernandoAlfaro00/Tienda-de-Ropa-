from django import forms

from .models import Perfil 

class ClienteForm(forms.ModelForm):

    class Meta:
        model=Perfil
        fields = ['usuario','es_astronauta',]