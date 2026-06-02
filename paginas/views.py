from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from articulos.models import Noticia, Comentario
from django.contrib.auth import get_user_model

# Obtenemos el modelo CustomUser de forma segura
User = get_user_model()

class DashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboard.html'

    def test_func(self):
        # Solo los usuarios marcados como 'staff' (administradores) pueden ver esto
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Recopilamos las estadísticas solicitadas en la rúbrica
        context['total_noticias'] = Noticia.objects.count()
        context['noticias_aprobadas'] = Noticia.objects.filter(aprobada=True).count()
        context['total_comentarios'] = Comentario.objects.count()
        context['total_usuarios'] = User.objects.count()
        return context