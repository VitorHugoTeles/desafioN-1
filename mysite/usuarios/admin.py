from django.contrib import admin
from .models import Usuario

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("username", "nome", "email")
    list_display_links = ("username", "nome")
    list_filter = ("nome",)
    search_fields = ("emai", "username")
admin.site.register(Usuario, UsuarioAdmin)