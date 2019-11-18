from django import forms
<<<<<<< HEAD
from .models import Perfil 
from django.contrib.auth.models import User
=======

from .models import Cliente
>>>>>>> 970d4daadbd2ecfc54575784de3c88d7d40e6a4e

class PerfilForm(forms.ModelForm):

    class Meta:
<<<<<<< HEAD
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
=======
        model = Cliente 
        fields = ('id','primer_nombre','segundo_nombre',
        'apellido_materno','apellido_paterno','run','email','telefono',
        'fecha_nacimiento','region','comuna','vivienda',)
   
>>>>>>> 970d4daadbd2ecfc54575784de3c88d7d40e6a4e
