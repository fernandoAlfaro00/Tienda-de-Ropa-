from django.urls import path
from .views import lista_productos ,agregar_productos ,editar_productos , eliminar_productos , index ,filtro_precio

urlpatterns = [
    path('', index , name='index' ),
    path('listadoProductos', lista_productos , name='listadoProductos'),
    path('AgregarProductos', agregar_productos ,name='AgregarProductos'),
    path('editarProductos/<int:id>', editar_productos ,name='editarProductos'),
    path('eliminarProductos/<int:producto_id>', eliminar_productos , name='eliminarProductos' ),
    path('filtrarPorPrecio', filtro_precio ),

    


]