from django.urls import path
from . import views
from rest_framework.urlpatterns import  format_suffix_patterns
urlpatterns = [
    path('api/', views.API_objects.as_view()),
    path('api/<int:pk>/', views.API_objects_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    path('', views.index , name='index' ),
    path('listadoProductos', views.lista_productos , name='listadoProductos'),
    path('AgregarProductos', views.agregar_productos ,name='AgregarProductos'),
    path('editarProductos/<int:id>', views.editar_productos ,name='editarProductos'),
    path('estadoProductos/<int:producto_id>', views.cambiar_estado , name='estadoProductos' ),
    path('catalogo', views.catalogo_producto , name='catalogoProducto' ),
    path('detalle/<int:id_producto>',  views.detalle_productos, name='detalle'),
    path('eliminarProducto/<int:producto_id>' ,  views.eliminar_productos , name='eliminarProductos'),


    


]
