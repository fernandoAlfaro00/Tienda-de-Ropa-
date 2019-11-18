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

REGION_CHOICES = [( 0, 'Región Metropolitana de Santiago'), ( 1, 'Región de Tarapacá'), (2, 'Región de Antofagasta'), (3, 'Región de Atacama'), (4, 'Región de Coquimbo'), (5, 'Región de Valparaíso'), (6, 'Región del Libertador Bernardo O \'Higgins'), (7, 'Región del Maule'), (8, 'Región del Bío Bío'), (9, 'Región de la Araucanía'), (10, 'Región de los Lagos'), (11, 'Región de Aysén del General Carlos Ibáñez del Campo'), (12, 'Región de Magallanes y la Antártica Chilena'), (13, 'Región de Los Ríos'), (14, 'Región de Arica-Parinacota')]

COMUNA_CHOICES = [('lr','La Reina'),('pu','Pudahue')]

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

