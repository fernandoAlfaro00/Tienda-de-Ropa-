from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente 
        fields = ('id','primer_nombre','segundo_nombre',
        'apellido_materno','apellido_paterno','run','email','telefono',
        'fecha_nacimiento','region','comuna','vivienda',)
   