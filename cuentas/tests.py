from django.test import TestCase
from django.contrib.auth import get_user_model

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