"""mispoleras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings 
from django.conf.urls.static import static

""" 

    path('admin/', admin.site.urls),
    path('', include('mantenedorProductos.urls')),
<<<<<<< HEAD
    path('', include('mantenedorUsuarios.urls')),
    
=======
    ###ojo aqui /ficha no es necesario cuando pones path('/ficha', include('mantenedorUsuarios.urls')),
    cuando hace path('', include('mantenedorProductos.urls'))  lo que esta haciendo es importar todas
    las urls definidas en  el mantenedor de usuario

>>>>>>> 970d4daadbd2ecfc54575784de3c88d7d40e6a4e
    
     """
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('mantenedorProductos.urls')),
    path('', include('mantenedorUsuarios.urls'))
    
    
    


    

]


urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


admin.site.site_header = "Adminitracion de Mis poleras"
admin.site.index_title = "Modulos"
admin.site.site_title =  "Mis Poleras"