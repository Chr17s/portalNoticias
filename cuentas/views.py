from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser

class RegistroUsuarioView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registro.html' # Este archivo HTML lo crearemos e integraremos con Bootstrap en la Fase 4

class EditarPerfilView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'perfil.html'
    fields = ['first_name', 'last_name', 'avatar', 'biografia']
    success_url = reverse_lazy('lista_noticias')

    # Este método asegura que el usuario SOLO pueda editar su propio perfil
    def get_object(self):
        return self.request.user    