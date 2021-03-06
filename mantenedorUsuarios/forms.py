from django import forms
from .models import Perfil , Comuna
from django.contrib.auth.models import User
from datetime  import datetime as dt 



class PerfilForm(forms.ModelForm):

    class Meta:
      
        model=Perfil
        fields = ['run' , 'telefono' ,'region', 'fecha_nacimiento','comuna','vivienda',]
        widgets = {
            'fecha_nacimiento' : forms.SelectDateWidget(years=range(1945 ,dt.today().year)) 
        }
        error_messages = {
            'run' :{
                'max_length': 'Maximo de 15 caracteres',
                'required':'Obligatorio'
            },
            'region' :{
                
                'required':'Por favor Seleccione una region ',

            },
            'comuna': {
                'required':'Por favor Seleccione una Comuna ',
                
            },
            'vivienda': {
                'required':'Por favor Seleccione una vivienda ',
                
            }
            ,
        }

       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # pylint: disable=no-member
        self.fields['comuna'].queryset = Comuna.objects.none()

        if 'region' in self.data:
                try:
                    region_id = int(self.data.get('region'))
                    self.fields['comuna'].queryset = Comuna.objects.filter(region_id=region_id).order_by('nombre')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
                self.fields['comuna'].queryset = self.instance.region.comuna_set.order_by('nombre')
        


class UsuarioForm(forms.ModelForm ):

    class Meta:
        model= User
        fields= ['username','password', 'email','first_name','last_name']
        labels =  {
            'username':'Usuario', 'password':'Contraseña', 'email':'Correo' , 'first_name' :  'Nombres' ,  'last_name' : 'apellidos' 
        }
        widgets = {
            'password': forms.PasswordInput(),
            'first_name': forms.TextInput(attrs={'name':'first_name' , 'max_length':'60' , 'min_length':'1'}),
            'last_name': forms.TextInput(attrs={'name':'last_name' , 'max_length':'60' , 'min_length':'1' }),
            'email': forms.EmailInput(attrs={'name':'email' , 'max_length':'60' , 'min_length':'1'}),
            'username': forms.TextInput(attrs={'name':'username' , 'max_length':'60' , 'min_length':'1'}),
        }   

        error_messages = {

            'password' :  {
                'required' :  'La Contraseña es Obligatoria ',
            },
            'first_name' : {
                'required': 'Ingrese el  nombre'
            },
            'last_name':{
                'required': 'Ingrese su apellido'
            }

        }
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("EL Email ya existe")
        return email

    
