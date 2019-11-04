from django import forms 
from .models import Producto
from colorful.forms import  ColorFieldWidget

class ProductoForm(forms.ModelForm):

    class Meta:
        model=Producto
        fields = ['nombre', 'codigo','precio_comprar','precio_venta','color','descuento','numero_talla','tipo_tela','descripcion' ,'imagen']
        labels = {
            'nombre':'Nombre  Producto', 'color':' Elige el color', 
        }
        widgets = {

            'precio_comprar': forms.NumberInput(attrs={
                'class':'form-group '
            }  ),
            'precio_venta': forms.NumberInput(
                attrs={
                    'class':'form-group col-md-6 mb-0'
                }
            ),
            'imagen' :  forms.ClearableFileInput(
                attrs={
                    'class':'form-group col-md-6 mb-0'
                }
            ),
            'nombre':forms.TextInput(
                attrs={
                'class':'col-xl-6 '
            } 
            ),
            'codigo':forms.NumberInput(
                attrs={
                'class':'col-xl-6 '
            } 
            ),
            'descuento': forms.NumberInput(
                attrs={
                'class':'form-group col-md-6 mb-0'
            } 
            ),
            'color': forms.Select(attrs={
                'class':'form-group col-md-6 mb-0'
            } ),

            'numero_talla':  forms.TextInput(
                attrs={
                'class':'form-group col-md-6 mb-0'
            } 
            ),
            'tipo_tela': forms.TextInput(attrs={
                'class':'form-group col-md-6 mb-0'
            } ),
            'descripcion':forms.Textarea(attrs={
                'class':'form-group col-md-6 mb-0'
            } ),
            
        }


        
