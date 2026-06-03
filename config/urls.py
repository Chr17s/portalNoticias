from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    # 1. URLs de Autenticación oficiales de Django (Login, Logout, Password Reset)
    path('cuentas/', include('django.contrib.auth.urls')),
    
    # 2. URLs personalizadas de nuestra app cuentas (Registro)
    path('cuentas/', include('cuentas.urls')),
    
    # 3. URLs de nuestra app principal (Noticias y Comentarios)
    path('', include('articulos.urls')),

    path('', include('paginas.urls')),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

# Configuración obligatoria para poder ver las imágenes subidas en entorno de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)