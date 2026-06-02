from django.urls import path
from .views import (
    ListaNoticiasView,
    DetalleNoticiaView,
    CrearNoticiaView,
    EditarNoticiaView,
    EliminarNoticiaView,
    CrearComentarioView,
    ParaTiView,
    me_gusta_noticia,
    leer_notificaciones,
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

    path('noticia/<int:pk>/like/', me_gusta_noticia, name='me_gusta_noticia'),

    path('para-ti/', ParaTiView.as_view(), name='para_ti'),
    path('notificaciones/leer/', leer_notificaciones, name='leer_notificaciones'),
]