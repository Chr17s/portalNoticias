from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class PruebasManejoUsuarios(TestCase):
    def test_create_usuario(self):
        Usuario = get_user_model()
        usuario = Usuario.objects.create_user(username='usuarioprueba', email='usuariopruebar@gmail.com', edad=25, password='passwordmuyseguro1234',)

        self.assertEqual(usuario.username, 'usuarioprueba')
        self.assertEqual(usuario.email, 'usuariopruebar@gmail.com')
        self.assertTrue(usuario.is_active)
        self.assertFalse(usuario.is_staff)
        self.assertFalse(usuario.is_superuser)

    def test_create_superusuario(self):
        Usuario = get_user_model()
        usuario_admin = Usuario.objects.create_superuser(username='superusuarioprueba',
                                                         email='superusuarioprueba@gmail.com',
                                                         password='passwordaunmasseguro',)
        
        self.assertEqual(usuario_admin.username, 'superusuarioprueba')
        self.assertEqual(usuario_admin.email, 'superusuarioprueba@gmail.com')
        self.assertTrue(usuario_admin.is_active)
        self.assertTrue(usuario_admin.is_staff)
        self.assertTrue(usuario_admin.is_superuser)
    
class PruebasPaginaRegistro(TestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta= self.client.get('/cuentas/signup/')
        self.assertEqual(respuesta.status_code, 200)

    def test_nombre_vista_registro(self):
        respuesta = self.client.get(reverse('signup'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, 'registration/signup.html')
    
    def test_formulario_registro(self):
        respuesta = self.client.post(reverse('signup'), {
            'username': 'usuarioprueba',
            'email': 'usuarioprueba@gmail.com',
            'password1': 'passwordmuyseguro1234',
            'password2': 'passwordmuyseguro1234',
        })
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'usuarioprueba')
        self.assertEqual(get_user_model().objects.all()[0].email, 'usuarioprueba@gmail.com')
                         