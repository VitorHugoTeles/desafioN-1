from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')
        extra_krawgs = {
            'senha' : {'write_only': True} 
        }