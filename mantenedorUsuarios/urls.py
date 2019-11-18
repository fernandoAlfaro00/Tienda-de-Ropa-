from django.urls import path , include
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('entrar', views.entrar, name='entrar'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir', views.salir, name='salir'),
    
    
=======
    #ojo aqui esta llamando de nuevo a la vista para agregar usuarios
    path('ficha', agregar_usuario ),
>>>>>>> 970d4daadbd2ecfc54575784de3c88d7d40e6a4e
 

]