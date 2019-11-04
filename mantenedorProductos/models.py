from django.db import models
from colorful.fields import RGBColorField

""" tengo que arreglkalllod """
class Producto(models.Model):
    nombre =  models.CharField(max_length=50 , null=False , blank=False)
    descripcion =  models.TextField(max_length=40, null=False ,blank=True )
    color = RGBColorField(colors=['#FF0000', '#00FF00', '#0000FF'])
    precio_comprar = models.IntegerField(null=False , blank=False)
    precio_venta = models.IntegerField(null=False ,  blank=False )
    numero_talla = models.CharField(max_length=40)
    codigo =  models.IntegerField(null=False)
    tipo_tela = models.CharField(max_length=40)
    descuento = models.FloatField()
    imagen = models.ImageField()
    cantidad =  models.IntegerField(default=0 , null=False  , blank=False )


    def __str__(self):
        
        return self.nombre

