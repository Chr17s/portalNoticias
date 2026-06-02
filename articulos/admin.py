from django.contrib import admin
from .models import Categoria, Noticia, Comentario

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

class NoticiaAdmin(admin.ModelAdmin):
    # list_display: Columnas que se verán en la tabla
    list_display = ('titulo', 'autor', 'categoria', 'fecha_publicacion', 'aprobada')
    
    # list_filter: Panel lateral para filtrar resultados
    list_filter = ('aprobada', 'categoria', 'fecha_publicacion')
    
    # search_fields: Barra de búsqueda superior
    search_fields = ('titulo', 'contenido')
    
    # Permite a los administradores aprobar noticias directamente desde la lista
    list_editable = ('aprobada',)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'noticia', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('contenido', 'usuario__username', 'noticia__titulo')

# Registramos los modelos con sus clases personalizadas
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Comentario, ComentarioAdmin)