from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect
from .forms import ProductoForm
from django.conf import settings
from .models  import Producto
from django.db.models  import Q
from .case import switch
from .serializers import ProductoSerializer
from rest_framework import generics
from django.contrib.auth.decorators import login_required ,permission_required
import os
from django.core.paginator import Paginator


    

def index(request):
    
    queryset = request.GET.get("buscar")
    # pylint: disable=no-member
    productos = Producto.objects.filter(estado= True )
    
    if queryset:
        
        productos = Producto.objects.filter( 
            Q(nombre__icontains = queryset)|
            Q(descripcion__icontains =queryset)
        ).distinct()
        
        return HttpResponseRedirect('catalogo')
    return render(request , 'app/index.html')

@login_required
@permission_required('mantenedorProductos.change_producto', raise_exception=True)
def lista_productos(request):
    # pylint: disable=no-member
    productos = Producto.objects.all()
    datos  = {'productos':productos}
    return render(request ,'app/listadoProducto.html',datos)

@login_required
@permission_required('mantenedorProductos.add_producto', raise_exception=True)
def agregar_productos(request):
    datos = {'form':ProductoForm()}
    if request.method == 'POST':

        form = ProductoForm(request.POST , files=request.FILES)

        if  form.is_valid():

            producto = form.save(commit=False)
            
            producto.save()
            
        datos['form'] = form
        

    return render(request , 'app/agregarProductos.html' , datos )

@login_required
@permission_required('mantenedorProducto.delete_producto', raise_exception=True) 
def eliminar_productos(request ,producto_id):

    # pylint: disable=no-member
    producto =  Producto.objects.get(id=producto_id)

    
        #os.remove(os.path.join(settings.MEDIA_ROOT ,str(producto.imagen)))
        
    
    producto.estado =  not producto.estado 

    producto.save()


@login_required
@permission_required('mantenedorProductos.change_producto', raise_exception=True)
def cambiar_estado(request ,producto_id):

    # pylint: disable=no-member
    producto =  Producto.objects.get(id=producto_id)

    
        #os.remove(os.path.join(settings.MEDIA_ROOT ,str(producto.imagen)))
        
    
    producto.estado =  not producto.estado 

    producto.save()

    return redirect('listadoProductos') 

@login_required
@permission_required('mantenedorProductos.change_producto', raise_exception=True)
def editar_productos(request , id): 
    # pylint: disable=no-member
    producto = Producto.objects.get(id=id)
    #nombre_imagen =  str(producto.imagen)
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




 


def catalogo_producto(request):
    
    queryset = request.GET.get("buscar")
    
    # pylint: disable=no-member
    productos = Producto.objects.filter(estado= True )
    
    if queryset:
        
        productos = Producto.objects.filter( 
            Q(nombre__icontains = queryset)|
            Q(descripcion__icontains =queryset)
        ).distinct()
        
    filtro = 0
    
    if request.POST.get('filtro'):
        filtro = request.POST.get('filtro')

        productos  = Producto.objects.all().order_by(switch(filtro))

    paginator = Paginator(productos, 5)
    page  = request.GET.get('page')
    productos =  paginator.get_page(page)
    return render(request, 'app/catalogo.html' ,{'productos':productos ,'filtro':filtro})



def detalle_productos(request, id_producto):

    # pylint: disable=no-member
    producto = Producto.objects.get(id=id_producto)

    return render(request , 'app/detalle.html' , {'p':producto} )



class  API_objects(generics.ListCreateAPIView):
    # pylint: disable=no-member

    queryset =  Producto.objects.all()
    serializer_class = ProductoSerializer


class  API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    # pylint: disable=no-member

    queryset =  Producto.objects.all()
    serializer_class = ProductoSerializer