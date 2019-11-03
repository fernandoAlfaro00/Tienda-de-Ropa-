from django.db import models
from colorful.fields import RGBColorField

class Producto(models.Model):
    nombre =  models.CharField(max_length=50 , null=False , blank=False)
    descripcion =  models.TextField(max_length=40, null=False ,blank=True )
    color = RGBColorField(colors=['#FF0000', '#00FF00', '#0000FF'])
    precio_comprar = models.IntegerField(null=False)
    precio_venta = models.IntegerField(null=False)
    numero_talla = models.CharField(max_length=40)
    codigo =  models.IntegerField()
    tipo_tela = models.CharField(max_length=40)
    descuento = models.FloatField()
    imagen = models.ImageField()
