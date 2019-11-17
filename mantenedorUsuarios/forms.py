from django import forms
from .models import Perfil 
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):

    class Meta:
        model=Perfil
        fields = ['run' , 'telefono' ,'region' , 'fecha_nacimiento','comuna','vivienda',]
        


class UsuarioForm(forms.ModelForm ):

    class Meta:
        model= User
        fields= ['username','password', 'email','first_name','last_name']
        labels =  {
            'username':'Usuario', 'password':'Contraseña', 'email':'Correo'
        }
        widgets = {
            'password': forms.PasswordInput(),

        }   
