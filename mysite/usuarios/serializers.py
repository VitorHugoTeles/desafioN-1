from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.hashers import make_password

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')
        extra_kwargs = {
            'password' : {'write_only': True}}
    def create(self, validated_data):
        # ADICIONE ESTA LINHA:
        print("==================================================")
        print("EXECUTANDO HASH DE SENHA PARA:", validated_data['username'])
        print("==================================================")

        # As linhas de hashing continuam
        validated_data['password'] = make_password(validated_data['password'])
        return super(UsuarioSerializer, self).create(validated_data) 