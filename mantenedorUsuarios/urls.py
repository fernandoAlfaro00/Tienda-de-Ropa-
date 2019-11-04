from django.urls import path
from .views import agregar_usuario

urlpatterns = [
    path('agregarUsuario', agregar_usuario ,name="registrousuarios" ),
 

]