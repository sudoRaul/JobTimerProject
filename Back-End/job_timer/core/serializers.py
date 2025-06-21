from rest_framework import serializers
from .models import Usuario, Departamento, Turno, Fichaje
from django.contrib.auth import get_user_model

User = get_user_model()

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'
        
class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model: Turno
        fields = '__all__'
        
        
class UsuarioSerializer(serializers.ModelSerializer):
    departamento = serializers.PrimaryKeyRelatedField(queryset=Departamento.objects.all())
    turno = serializers.PrimaryKeyRelatedField(queryset=Turno.objects.all())
    
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'rol', 'departamento', 'turno']
        
        

class FichajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fichaje
        fields = '__all__'