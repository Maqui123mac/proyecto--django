from django.shortcuts import render
from.models import Alumnos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from  django.shortcuts import get_object_or_404



# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()

    return render(request, "registros/principal.html",{"9B":alumnos})
#Indicamos el lugar se redenrizara

def registrar(request):
    if request.method =='POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return render(request,'registros/contacto.html')
        comentarios = ComentarioContacto.objects.all() 
        return render(request,"registros/comentario.html", {'comentario':comentarios})

    form = ComentarioContactoForm()
#Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form': form})
    
    
def contacto(request):
    return render(request,"registros/contacto.html")


def comentario(request):
   comentario = ComentarioContacto.objects.all()
   return render(request, "registros/comentario.html",{"comentario":comentario})



def eliminarComentarioContacto(request,id,
    confirmacion='registro/confirmarEliminacion.html'):
    comentario =  get_object_or_404(ComentarioContacto,id=id)
    if request.method =="POST":
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request,"registros/comentario.html" ,{"comentarios": comentarios})
    return render(request,confirmacion,{"object":comentario})

def consultarComentarioIndivivual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    return render(request,"registros/formularioeditar.html", {'comentario':comentario})

def editarComentarioContacto(request,id):
    comentario =  get_object_or_404(ComentarioContacto,id=id)
    form = ComentarioContactoForm(request.POST,instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/contacto.html",{'comentario':comentarios})
        
    return render(request,"registros/formularioeditar.html",{'comentario':comentario})
   
   








