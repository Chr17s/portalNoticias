from django.urls import path
from .views import (
    ListaNoticiasView,
    DetalleNoticiaView,
    CrearNoticiaView,
    EditarNoticiaView,
    EliminarNoticiaView,
    CrearComentarioView
)

urlpatterns = [
    # CRUD de Noticias
    path('', ListaNoticiasView.as_view(), name='lista_noticias'),
    path('noticia/<int:pk>/', DetalleNoticiaView.as_view(), name='detalle_noticia'),
    path('noticia/nueva/', CrearNoticiaView.as_view(), name='crear_noticia'),
    path('noticia/<int:pk>/editar/', EditarNoticiaView.as_view(), name='editar_noticia'),
    path('noticia/<int:pk>/eliminar/', EliminarNoticiaView.as_view(), name='eliminar_noticia'),
    
    # Comentarios
    path('noticia/<int:pk>/comentar/', CrearComentarioView.as_view(), name='crear_comentario'),
]