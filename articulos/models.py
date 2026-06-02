from django.db import models
from django.conf import settings
from django.urls import reverse

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fuente_url = models.URLField(blank=True, null=True)
    aprobada = models.BooleanField(default=False)
    
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='noticias')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='noticias')
    
    # NUEVO: Campo para la Opción 1 (Me gusta)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='noticias_gustadas', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('detalle_noticia', kwargs={'pk': self.pk})

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.noticia.titulo}"