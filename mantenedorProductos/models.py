from django.db import models
from colorful.fields import RGBColorField
from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
class ModeloBase(models.Model):
    
    id = models.AutoField(primary_key = True)
    estado = models.BooleanField('Estado', default= True)
    fecha_creacion = models.DateField(auto_now= False, auto_now_add= True)
    fecha_modificacion = models.DateField(auto_now=True  ,   auto_now_add=False)
    fecha_eliminacion = models.DateField(auto_now=True  ,   auto_now_add=False)
    class Meta :
        abstract = True 



class Producto(ModeloBase):
    nombre =  models.CharField(max_length=50 , null=False , blank=False)
    descripcion =  models.TextField(max_length=40, null=False ,blank=True )
    marca   =  models.CharField(max_length=50 ,  blank=False ,  null=False)
    color = RGBColorField(colors=['#FF0000', '#00FF00', '#0000FF'])
    precio_comprar = models.IntegerField(null=False , blank=False)
    precio_venta = models.IntegerField(null=False ,  blank=False )
    numero_talla = models.CharField(max_length=40)
    codigo =  models.IntegerField(null=False)
    tipo_tela = models.CharField(max_length=40)
    descuento = models.FloatField(default=0 )
    imagen = models.ImageField()
    cantidad =  models.IntegerField(default=0 , null=False  , blank=False )

    def __str__(self):
        
        return self.nombre

    def clean_descuento(self):

        if (self.descuento < 0):

            raise ValidationError("el descuento tiene que ser un numero positivo")
        elif (self.descuento > 100):

            raise  ValidationError("El descuento  no puede ser mayor a 100%")
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    


	
 