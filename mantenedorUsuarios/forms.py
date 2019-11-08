from django import forms
from .models import Perfil 

class ClienteForm(forms.ModelForm):

    class Meta:
        model=Perfil
        fields = ['username','es_astronauta', 'password' , 'email']