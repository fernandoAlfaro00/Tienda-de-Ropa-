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
               
            }  ),
            'precio_venta': forms.NumberInput(
                attrs={
                                    }
            ),
            'imagen' :  forms.ClearableFileInput(
                attrs={
                    
                }
            ),
            'nombre':forms.TextInput(
                attrs={
                
            } 
            ),
            'codigo':forms.NumberInput(
                attrs={
                
            } 
            ),
            'descuento': forms.NumberInput(
                attrs={
                
            } 
            ),
            'color': forms.Select(attrs={
                
            } ),

            'numero_talla':  forms.TextInput(
                attrs={
                
            } 
            ),
            'tipo_tela': forms.TextInput(attrs={
                
            } ),
            'descripcion':forms.Textarea(attrs={
                
            } ),
            
        }


        
