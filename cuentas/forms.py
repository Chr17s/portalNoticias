# cuentas/forms.py

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class FormularioCreacionUsuario(UserCreationForm):
    class Meta:
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('edad',)

class FormularioModificacionUsuario(UserChangeForm):
    class Meta:
        model = Usuario
        fields = UserChangeForm.Meta.fields

