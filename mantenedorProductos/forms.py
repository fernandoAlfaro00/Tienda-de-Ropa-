from django import forms

from .models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model=Producto
        fields = ['nombre','precio_comprar','precio_venta','color','descripcion','descuento','numero_talla','tipo_tela','codigo','imagen']