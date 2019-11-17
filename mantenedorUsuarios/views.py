from django.http  import HttpResponse
from django.shortcuts import render ,redirect
from .forms  import PerfilForm , UsuarioForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  login , logout ,authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



def signup(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        usuario_form =  UsuarioForm(request.POST)
        perfil_form =  PerfilForm(request.POST)
        
        if usuario_form.is_valid() and perfil_form.is_valid():
           
            usuario =  usuario_form.save()

            usuario.set_password(usuario.password)
            
            usuario.save()
           
            print("entrando a perfil")

            perfil = perfil_form.save(commit=False)
            
            perfil.usuario  = usuario

            perfil.save()
            
            return redirect('home')
    else:
        usuario_form =  UsuarioForm(request.POST)
        perfil_form =  PerfilForm(request.POST)
    return render(request, 'registration/signup.html', {
        'usuario_form': usuario_form, 'perfil_form':perfil_form
    })




def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })




@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'
