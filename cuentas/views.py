from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

class RegistroUsuarioView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registro.html' # Este archivo HTML lo crearemos e integraremos con Bootstrap en la Fase 4