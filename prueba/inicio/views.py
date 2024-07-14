from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render 

#menu="""""""




# Create your views here.
def Principal(request):
    return render(request,"inicio/principal.html")

'''def contacto(request):
   
    return render(request,"inicio/contacto.html")'''

def formulario(request):
    
        
   return render(request,"inicio/formulario.html")

def ejemplo(request):
    
        
   return render(request,"inicio/ejemplo.html")





