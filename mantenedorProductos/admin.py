from .models import Producto
from django.contrib import admin

class  ProductoAdmin(admin.ModelAdmin ):

    #list_display =[]
    #search_fields = ['nombre' , 'marca']
    #list_filter = [ 'marca']
    list_per_page = 10

admin.site.register(Producto , ProductoAdmin)