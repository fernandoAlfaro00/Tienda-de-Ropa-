from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='index' ),
    path('listadoProductos', views.lista_productos , name='listadoProductos'),
    path('AgregarProductos', views.agregar_productos ,name='AgregarProductos'),
    path('editarProductos/<int:id>', views.editar_productos ,name='editarProductos'),
    path('eliminarProductos/<int:producto_id>', views.eliminar_productos , name='eliminarProductos' ),
    path('filtrarPorPrecio', views.filtro_precio ),
    path('catalogo', views.catalogo_producto , name='catalogoProducto' ),


    


]
