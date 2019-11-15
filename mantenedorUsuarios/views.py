from django.shortcuts import render ,redirect
from .forms  import ClienteForm
from .models import Perfil
def agregar_usuario(request):

    if request.method == "POST":
        form = ClienteForm(request.POST , files=request.FILES)

        if  form.is_valid():
           
            model_instance = form.save(commit=False)
            model_instance.save()
            
            return redirect('/')

    else:
        form  = ClienteForm()
        return render(request , 'app/regpruebas.html' , {'form':form})


def  listar_usuario(request):
    form =  Perfil.objects.all()
    datos = {'form':form } 
    return  render(request ,  'app/listadoClientes.html' , datos  )

