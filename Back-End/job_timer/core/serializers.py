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
    
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'first_name', 'last_name',
                  'email', 'password', 'rol', 'departamento',
                  'turno', 'departamento_id', 'turno_id']
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)
        user.save()
        return user
        
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