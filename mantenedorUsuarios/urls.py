from django.urls import path
from .views import agregar_usuario

urlpatterns = [
    #ojo aqui esta llamando de nuevo a la vista para agregar usuarios
    path('ficha', agregar_usuario ),
    path('ficha/agregarUsuario', agregar_usuario ),
 

]