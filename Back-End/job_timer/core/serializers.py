from rest_framework import serializers
from .models import Usuario, Departamento, Turno, Fichaje
from django.contrib.auth import get_user_model

User = get_user_model()

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'
        
        
class DepartamentoResumeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Departamento
        fields = ['id', 'nombre']
        
        
class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'
        
class TurnoResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ['id', 'nombre']
        
        
class UsuarioSerializer(serializers.ModelSerializer):
    departamento = DepartamentoResumeSerializer(read_only= True)
    turno = TurnoResumeSerializer(read_only=True)
    
    departamento_id = serializers.PrimaryKeyRelatedField(
        queryset = Departamento.objects.all(), write_only = True, source = 'departamento'
    )
    
    turno_id = serializers.PrimaryKeyRelatedField(
        queryset = Turno.objects.all(), write_only = True, source = 'turno'
    )
    
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'rol', 'departamento', 'turno', 'departamento_id', 'turno_id']
        
        
class UsuarioResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'first_name', 'last_name', 'email']
        
        

class FichajeSerializer(serializers.ModelSerializer):
    usuario = UsuarioResumeSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset = Usuario.objects.all(), write_only=True, source='usuario'
    )
    class Meta:
        model = Fichaje
        fields = ['id', 'usuario', 'usuario_id', 'tipo', 'fecha', 'hora']
        read_only_fields = ['fecha', 'hora']