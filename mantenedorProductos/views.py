from django.shortcuts import render ,redirect
from .forms import ProductoForm
from .models import Producto
from django.conf import settings
from paquetex.switchcase import switch
import os


def index(request):

    return render(request , 'app/index.html')

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
            
            return redirect('/AgregarProductos')

    else:
        form  = ProductoForm()
        return render(request , 'app/agregarProductos.html' , {'form':form})


def eliminar_productos(request ,producto_id):

    producto =  Producto.objects.get(id=producto_id)

    try:
        os.remove(os.path.join(settings.MEDIA_ROOT ,str(producto.imagen)))
        
    finally:
         producto.delete() 
   

   


    return redirect('/listadoProductos') 


def editar_productos(request , id): 

    producto = Producto.objects.get(id=id)
    nombre_imagen =  str(producto.imagen)
    form =  ProductoForm(instance=producto)

    if request.method == 'POST':

        #ver como se elimina la imagen 
        form = ProductoForm(request.POST , instance=producto ,  files=request.FILES)

        if form.is_valid():
            
           #os.remove(os.path.join(settings.MEDIA_ROOT ,nombre_imagen))
            producto = form.save(commit=False)
            
            producto.save()

            form = ProductoForm(instance=producto)

    return render(request , 'app/editarProductos.html',{'form':form})



def  filtro_precio(request):

   
    productos  = Producto.objects.all()
    filtro = 0
    
    if request.POST.get('filtro'):
        filtro = request.POST.get('filtro')

        productos  = Producto.objects.all().order_by(switch(filtro))

    return render(request, 'app/listadoProducto.html',{'productos':productos ,'filtro':filtro})



def catalogo_producto(request):
    
    return render(request, 'app/catalogo.html' ,{})