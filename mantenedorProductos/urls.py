from django.urls import path
from .views import lista_productos ,agregar_productos

urlpatterns = [
    path('listadoProductos', lista_productos),
    path('AgregarProductos', agregar_productos),

]