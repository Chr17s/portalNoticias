from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Noticia, Categoria, Comentario, Notificacion

# --- Vistas del CRUD de Noticias ---

class ListaNoticiasView(ListView):
    model = Noticia
    template_name = 'lista_noticias.html'
    context_object_name = 'noticias'
    paginate_by = 6

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
    # ... deja tus atributos de clase igual ...
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        noticia = get_object_or_404(Noticia, pk=self.kwargs['pk'])
        form.instance.noticia = noticia
        
        # NUEVO: Generar Notificación de Comentario
        if self.request.user != noticia.autor:
            Notificacion.objects.create(
                usuario=noticia.autor,
                mensaje=f"{self.request.user.username} comentó: '{form.instance.contenido[:20]}...'",
                url=noticia.get_absolute_url()
            )
            
        return super().form_valid(form)
    
@login_required
def me_gusta_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if noticia.likes.filter(id=request.user.id).exists():
        noticia.likes.remove(request.user)
    else:
        noticia.likes.add(request.user)
        # NUEVO: Generar Notificación de Like
        if request.user != noticia.autor:
            Notificacion.objects.create(
                usuario=noticia.autor,
                mensaje=f"A {request.user.username} le gustó tu noticia '{noticia.titulo}'.",
                url=noticia.get_absolute_url()
            )
    return redirect('detalle_noticia', pk=pk)

class ParaTiView(LoginRequiredMixin, ListView):
    model = Noticia
    template_name = 'lista_noticias.html'
    context_object_name = 'noticias'
    paginate_by = 6

    def get_queryset(self):
        # Algoritmo: Busca las categorías de las noticias que ya te gustaron
        categorias_gustadas = Categoria.objects.filter(noticias__likes=self.request.user).distinct()
        # Te recomienda noticias de esas categorías que NO hayas escrito tú
        return Noticia.objects.filter(categoria__in=categorias_gustadas).exclude(autor=self.request.user).order_by('-fecha_publicacion')

@login_required
def leer_notificaciones(request):
    # Marca todas las notificaciones del usuario como leídas
    request.user.notificaciones.filter(leida=False).update(leida=True)
    return redirect(request.META.get('HTTP_REFERER', 'lista_noticias'))