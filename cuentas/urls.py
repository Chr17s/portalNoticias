from django.urls import path
from .views import RegistroUsuarioView, EditarPerfilView

urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('perfil/', EditarPerfilView.as_view(), name='perfil'), # <--- NUEVA RUTA
]