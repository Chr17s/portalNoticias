from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import FormularioCreacionUsuario, FormularioModificacionUsuario
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    add_form = FormularioCreacionUsuario
    form = FormularioModificacionUsuario
    model = Usuario
    list_display = [ 'email', 'username', 'edad', 'is_staff']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('edad',)}),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'edad', 'password1', 'password2'),
        }),
    )

# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)