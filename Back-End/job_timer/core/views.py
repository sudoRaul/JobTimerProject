from django.shortcuts import render
from .models import Usuario, Departamento, Turno, Fichaje
from .serializers import UsuarioSerializer, DepartamentoSerializer, TurnoSerializer, FichajeSerializer
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.response import Response


User = get_user_model()

# Create your views here.

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    
    
class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer
    

class FichajeViewSet(viewsets.ModelViewSet):
    queryset = Fichaje.objects.all()
    serializer_class = FichajeSerializer
    

class UsuarioViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = User.objects.all()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UsuarioSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=404)
