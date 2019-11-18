from django import forms
from .models import Perfil , Comuna
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):

    class Meta:
        model=Perfil
        fields = ['run' , 'telefono' ,'region' , 'fecha_nacimiento','comuna','vivienda',]
        widgets = {
            'comuna' : forms.Select(attrs={'id':'id_comuna' , }),
            'region' : forms.Select(attrs={'id':'id_region' , }),
            'fecha_nacimiento': forms.DateInput(),

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
            'username':'Usuario', 'password':'Contraseña', 'email':'Correo'
        }
        widgets = {
            'password': forms.PasswordInput(),


        }   
     
    
    