from django import forms 
from .models import Producto
from django.core.validators import validate_integer
from django.core.files.images import get_image_dimensions
from colorfield.fields import ColorWidget ,ColorField

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
            'color':  forms.Select(),

            'numero_talla':  forms.TextInput(
                attrs={
                
            } 
            ),
            'tipo_tela': forms.TextInput(attrs={
                
            } ),
            'descripcion':forms.Textarea(attrs={
                
            } ),
            
        }

    
    def clean_imagen(self):
              
       img = self.cleaned_data.get("imagen")
       high = 225
       wide = 225
       w, h = get_image_dimensions(img)

       if w != wide:
           raise forms.ValidationError("La imagen tiene %i pixel ancho. debe tener %ipx de ancho" % (w, wide) )
       if h != high:
           raise forms.ValidationError("La imagen tiene %i pixel alto. debe tener %ipx de alto"  % (h, high) )
            
       return img
        
