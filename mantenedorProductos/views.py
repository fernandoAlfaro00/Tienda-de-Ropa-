from django.shortcuts import render ,redirect
from .forms import ProductoForm
from .models import Producto
def lista_productos(request):
    productos = Producto.objects.all()
    datos  = {'productos':productos}

    return render(request ,'app/listadoProducto.html',datos)


def agregar_productos(request):

    if request.method == "POST":
        form = ProductoForm(request.POST , files=request.FILES)

        if  form.is_valid():
           
            model_instance = form.save(commit=False)
            model_instance.save()
            
            return redirect('AgregarProductos')

    else:
        form  = ProductoForm()
        return render(request , 'app/agregarProductos.html' , {'form':form})
