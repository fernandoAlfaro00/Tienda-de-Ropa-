from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre =  models.CharField(max_length=40)
    descripcion =  models.TextField(max_length=40)
    color = models.CharField(max_length=12)
    precio_comprar = models.IntegerField()
    precio_venta = models.IntegerField()
    numero_talla = models.CharField(max_length=40)
    codigo =  models.IntegerField()
    tipo_tela = models.CharField(max_length=40)
    descuento = models.FloatField()
    imagen = models.ImageField()
