from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from articulos.models import Noticia, Comentario, Categoria
from django.contrib.auth import get_user_model

User = get_user_model()

class DashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboard.html'

    def test_func(self):
        # Permite el acceso solo a administradores
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Métricas Globales
        context['total_noticias'] = Noticia.objects.count()
        context['total_usuarios'] = User.objects.count()
        context['total_comentarios'] = Comentario.objects.count()
        
        # Total de Likes (Contando las relaciones en la tabla intermedia)
        context['total_likes'] = Noticia.likes.through.objects.count()
        
        # Desglose de Noticias por Categoría
        context['categorias_stats'] = Categoria.objects.annotate(total=Count('noticias'))
        
        return context