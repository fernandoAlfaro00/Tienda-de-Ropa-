def switch(opcion):



    if  not isinstance(opcion,str):


        opcion = str(opcion)

    def precio_mayor():

        return '-precio_venta'

    def precio_menor():

        return 'precio_venta'

    def default():

        return 'nombre'

    dict = {
        '1': precio_menor ,
        '2': precio_mayor ,
        '3': default 
    }

    return dict.get(opcion , default)()
    


    
