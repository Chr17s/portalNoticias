from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Noticia, Categoria, Comentario

User = get_user_model()

class PortalNoticiasTests(TestCase):
    def setUp(self):
        # Configuración inicial: Se ejecuta antes de cada prueba
        
        # 1. Crear un usuario de prueba
        self.user = User.objects.create_user(username='tester', password='password123', email='test@test.com')
        
        # 2. Crear una categoría de prueba
        self.categoria = Categoria.objects.create(nombre='Tecnología', descripcion='Noticias Tech')
        
        # 3. Crear una noticia de prueba
        self.noticia = Noticia.objects.create(
            titulo='Noticia de Prueba',
            contenido='Este es el contenido de la prueba automatizada.',
            autor=self.user,
            categoria=self.categoria
        )

    # Prueba 1: Creación de usuario
    def test_creacion_usuario(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(id=self.user.id).username, 'tester')

    # Prueba 2: Creación de noticia
    def test_creacion_noticia(self):
        self.assertEqual(Noticia.objects.count(), 1)
        self.assertEqual(self.noticia.titulo, 'Noticia de Prueba')

    # Prueba 3: Creación de comentario
    def test_creacion_comentario(self):
        comentario = Comentario.objects.create(
            noticia=self.noticia,
            usuario=self.user,
            contenido='Excelente artículo.'
        )
        self.assertEqual(Comentario.objects.count(), 1)
        self.assertEqual(comentario.contenido, 'Excelente artículo.')

    # Prueba 4: Acceso a vistas protegidas (Seguridad)
    def test_acceso_vista_protegida_sin_login(self):
        # Intentar acceder a la URL de crear noticia SIN iniciar sesión
        response = self.client.get(reverse('crear_noticia'))
        
        # Debe ser redirigido (Código 302) a la página de login
        self.assertEqual(response.status_code, 302)
        self.assertIn('login', response.url)

    # Prueba 5: Búsqueda de noticias
    def test_busqueda_noticias(self):
        # Buscar una palabra que SÍ existe en nuestra noticia
        response_exito = self.client.get(reverse('lista_noticias') + '?q=Prueba')
        self.assertContains(response_exito, 'Noticia de Prueba')
        
        # Buscar una palabra que NO existe
        response_vacia = self.client.get(reverse('lista_noticias') + '?q=Inexistente')
        self.assertNotContains(response_vacia, 'Noticia de Prueba')
        self.assertContains(response_vacia, 'Aún no hay noticias publicadas')