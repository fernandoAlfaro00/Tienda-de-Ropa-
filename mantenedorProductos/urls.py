from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='index' ),
    path('listadoProductos', views.lista_productos , name='listadoProductos'),
    path('AgregarProductos', views.agregar_productos ,name='AgregarProductos'),
    path('editarProductos/<int:id>', views.editar_productos ,name='editarProductos'),
    path('estadoProductos/<int:producto_id>', views.cambiar_estado , name='estadoProductos' ),
    path('catalogo', views.catalogo_producto , name='catalogoProducto' ),
    path('detalle/<int:id_producto>',  views.detalle_productos, name='detalle'),


    


]
