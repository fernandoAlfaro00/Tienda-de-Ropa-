from django.urls import path , include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('entrar', views.entrar, name='entrar'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir', views.salir, name='salir'),   
    path('ajax/cargar-Comuna/', views.cargar_Comunas , name='ajax_cargar_comunas'),


]