# Generated by Django 2.2.6 on 2019-11-04 15:23

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedorUsuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=40)),
                ('segundo_nombre', models.CharField(max_length=40)),
                ('apellido_materno', models.CharField(max_length=40)),
                ('apellido_paterno', models.CharField(max_length=40)),
                ('run', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('fecha_nacimiento', models.DateField()),
                ('region', models.IntegerField(choices=[(0, 'Región Metropolitana de Santiago'), (1, 'Región de Tarapacá'), (2, 'Región de Antofagasta'), (3, 'Región de Atacama'), (4, 'Región de Coquimbo'), (5, 'Región de Valparaíso'), (6, "Región del Libertador Bernardo O 'Higgins"), (7, 'Región del Maule'), (8, 'Región del Bío Bío'), (9, 'Región de la Araucanía'), (10, 'Región de los Lagos'), (11, 'Región de Aysén del General Carlos Ibáñez del Campo'), (12, 'Región de Magallanes y la Antártica Chilena'), (13, 'Región de Los Ríos'), (14, 'Región de Arica-Parinacota')], null=True)),
                ('comuna', models.CharField(choices=[('lr', 'La Reina'), ('pu', 'Pudahue')], max_length=50, null=True)),
                ('vivienda', models.IntegerField(choices=[(1, 'Casa con patio Grande'), (2, 'Casa con patio Pequeño'), (3, 'Casa sin Patio'), (4, 'Departamento')], null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
