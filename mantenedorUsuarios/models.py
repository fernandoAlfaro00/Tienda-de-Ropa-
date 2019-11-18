from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class Region(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
class  Comuna(models.Model):
    nombre = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

VIVENDA_CHOICES =[(1,'Casa con patio Grande'),
    (2,'Casa con patio Pequeño'),
    (3,'Casa sin Patio'),
    (4,'Departamento')]


class Perfil(models.Model):
    usuario = models.OneToOneField( User, on_delete=models.CASCADE)
    run = models.CharField(max_length=15)
    telefono = PhoneNumberField()
    fecha_nacimiento = models.DateField(null=True)
    region = models.ForeignKey(Region , on_delete=models.SET_NULL , null=True)
    comuna = models.ForeignKey(Comuna , on_delete=models.SET_NULL , null=True)
    vivienda = models.IntegerField(choices=VIVENDA_CHOICES , null=True)

