from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db.models import Q
from .models import Noticia, Categoria, Comentario

# --- Vistas del CRUD de Noticias ---

class ListaNoticiasView(ListView):
    model = Noticia
    template_name = 'lista_noticias.html'
    context_object_name = 'noticias'

    def get_queryset(self):
        # 1. Obtener todas las noticias ordenadas por las más recientes
        queryset = Noticia.objects.all().order_by('-fecha_publicacion')
        
        # 2. Capturar los términos de búsqueda de la URL (?q=... & categoria=...)
        query = self.request.GET.get('q')
        categoria_id = self.request.GET.get('categoria')

        # 3. Aplicar filtro de búsqueda por texto (en título O en categoría)
        if query:
            queryset = queryset.filter(
                Q(titulo__icontains=query) | 
                Q(categoria__nombre__icontains=query)
            )
            
        # 4. Aplicar filtro exacto por categoría si el usuario hace clic en una
        if categoria_id:
            queryset = queryset.filter(categoria__id=categoria_id)

        return queryset

    def get_context_data(self, **kwargs):
        # Inyectar la lista de todas las categorías para pintar el menú de filtros
        context = super().get_context_data(**kwargs)
        context['categorias_list'] = Categoria.objects.all()
        return context

class DetalleNoticiaView(DetailView):
    model = Noticia
    template_name = 'detalle_noticia.html'

# Busca esta clase en articulos/views.py y actualízala así:
class CrearNoticiaView(LoginRequiredMixin, CreateView):
    model = Noticia
    template_name = 'crear_noticia.html'
    fields = ['titulo', 'contenido', 'imagen', 'fuente_url', 'categoria']
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
class EditarNoticiaView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Noticia
    template_name = 'editar_noticia.html'
    fields = ['titulo', 'contenido', 'imagen', 'fuente_url', 'categoria']

    def test_func(self):
        noticia = self.get_object()
        # Solo permite editar si el usuario es el autor o un superusuario (admin)
        return self.request.user == noticia.autor or self.request.user.is_superuser

class EliminarNoticiaView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Noticia
    template_name = 'eliminar_noticia.html'
    success_url = reverse_lazy('lista_noticias')

    def test_func(self):
        noticia = self.get_object()
        # Solo permite eliminar si el usuario es el autor o un superusuario (admin)
        return self.request.user == noticia.autor or self.request.user.is_superuser

# --- Vistas de Comentarios ---

class CrearComentarioView(LoginRequiredMixin, CreateView):
    model = Comentario
    template_name = 'crear_comentario.html'
    fields = ['contenido'] 
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.noticia = get_object_or_404(Noticia, pk=self.kwargs['pk'])
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('detalle_noticia', kwargs={'pk': self.kwargs['pk']})