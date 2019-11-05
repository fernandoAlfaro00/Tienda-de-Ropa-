from django.urls import path
from .views import agregar_usuario

urlpatterns = [
    path('ficha', agregar_usuario ),
    path('ficha/agregarUsuario', agregar_usuario ),
 

]