from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import FormularioCreacionUsuario


# Create your views here.
class VistaRegistro(CreateView):
    template_name = 'registration/signup.html'
    form_class = FormularioCreacionUsuario
    success_url = reverse_lazy('login')