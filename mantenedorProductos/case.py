def switch(opcion):



    if  not isinstance(opcion,str):


        opcion = str(opcion)

    def precio_mayor():

        return '-precio_venta'

    def precio_menor():

        return 'precio_venta'
    def nombre_desc():
        
        return '-nombre'
    def  marca_asc():

        return 'marca'

    def marca_desc():

        return '-marca'

    def default():

        return 'nombre'

    dict = {
        '0': default,
        '1': precio_menor ,
        '2': precio_mayor ,
        '3': nombre_desc,
        '4':marca_asc,
        '5':marca_desc,
    }

    return dict.get(opcion , default)()
    


    
