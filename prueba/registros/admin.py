from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto

# Register your models here.


class AdministrarModelo(admin.ModelAdmin):

    readonly_fields=('created', 'updated')
    list_display=('matricula', 'nombre', 'carrera', 'turno')
    search_fields=('matricula','nombre', 'carrera', 'turno')
    date_hierarchy='created'
    list_per_page=2
    list_display_links=('matricula','nombre')
    list_editable=('turno',)

admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentario(admin.ModelAdmin):

    readonly_fields=('created', 'id')
    list_display=('id', 'coment')
    search_fields=('id','created')
    date_hierarchy='created'


admin.site.register(Comentario, AdministrarComentario)


class AdministrarComentarioContacto(admin.ModelAdmin):

    readonly_fields=('usuario', 'mensaje')
    list_display=('usuario', 'mensaje')
    search_fields=('usuario','mensaje')
    
admin.site.register(ComentarioContacto, AdministrarComentarioContacto)