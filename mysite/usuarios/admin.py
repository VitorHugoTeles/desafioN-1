from django.contrib import admin
from .models import Usuario
 
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'nome', 'email')
    search_fields = ('username', 'email', 'nome')
    fieldsets = (
        (None, {'fields': ('username', 'password')}), 
        ('Informações Pessoais', {'fields': ('nome', 'email')}),)
    readonly_fields = ('password',) 
    
admin.site.register(Usuario, UsuarioAdmin)