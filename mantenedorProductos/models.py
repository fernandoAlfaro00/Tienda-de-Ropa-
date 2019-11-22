from django.db import models
from colorful.fields import RGBColorField
from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator 
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
    precio_comprar = models.PositiveIntegerField(default=10, validators=[MinValueValidator(0)])
    precio_venta = models.IntegerField(null=False ,  blank=False ,  validators=[MinValueValidator(0)] )
    numero_talla = models.CharField(max_length=40)
    codigo =  models.IntegerField(null=False)
    tipo_tela = models.CharField(max_length=40)
    descuento = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
    imagen = models.ImageField()
    cantidad =  models.IntegerField(default=0 , null=False  , blank=False )

    def __str__(self):
        
        return self.nombre

   
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    


	
 