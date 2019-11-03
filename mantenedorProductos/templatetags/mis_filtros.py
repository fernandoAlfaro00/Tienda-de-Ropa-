from django.template  import  Library 


register =  Library()


def color_fondo(elemento , color):

   return  elemento.as_widget(attrs={"class":color})


register.filter('bgColor',color_fondo)