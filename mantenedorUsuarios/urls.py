from django.urls import path
from .views import agregar_usuario , listar_usuario

urlpatterns = [
    path('agregarUsuario', agregar_usuario ,name="registrousuarios" ),
    path('listadoUsuario', listar_usuario ,name="listadousuario" ),

 

]