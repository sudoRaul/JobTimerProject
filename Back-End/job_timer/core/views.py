from django.shortcuts import render
from .models import Usuario, Departamento, Turno, Fichaje
from .serializers import UsuarioSerializer, DepartamentoSerializer, TurnoSerializer, FichajeSerializer, UsuarioResumeSerializer
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action



User = get_user_model()

# Create your views here.

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    
    def list(self, request):
        queryset = Departamento.objects.all()
        serializer = DepartamentoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            departamento = Departamento.objects.get(pk = pk)
            serializer = DepartamentoSerializer(departamento)
            return Response(serializer.data)
        except Departamento.DoesNotExist:
            return Response({"error": "Departamento no encontrado"}, status=404)
    
    
    def create(self, request):
        serializer = DepartamentoSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({"error": "Departamento no encontrado"}, status=404)
    
        serializer = DepartamentoSerializer(departamento, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:
            departamento = Departamento.objects.get(pk=pk)
            departamento.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Departamento.DoesNotExist:
            return Response({"error": "Departamento no encontrado"}, status=404)
        
    
    @action(detail=True, methods=['get'], url_path='usuarios')
    def listar_usuarios(self, request, pk=None):
        departamento = self.get_object()
        usuarios = Usuario.objects.filter(departamento = departamento)
        serializer = UsuarioResumeSerializer(usuarios, many=True)
        return Response(serializer.data)
    
class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer
    
    def list(self, request):   
        queryset = Turno.objects.all()
        serializer = TurnoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            turno = Turno.objects.get(pk=pk)
            serializer = TurnoSerializer(turno)
            return Response(serializer.data)
        except Turno.DoesNotExist:
            return Response({"error": "Turno no encontrado"}, status=404)
        
        
    def create(self, request):
        serializer = TurnoSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        try:
            turno = Turno.objects.get(pk=pk)
        except Turno.DoesNotExist:
            return Response({"error": "Turno no encontrado"}, status=404)
        
        serializer = TurnoSerializer(turno, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def destroy(self, request, pk=None):
        try:
            turno = Turno.objects.get(pk=pk)
            turno.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Turno.DoesNotExist:
            return Response({"error": "Turno no encontrado"}, status=404)
        
    @action(detail=True, methods=['get'], url_path='usuarios')
    def listar_usuarios(self, request, pk = None):
        turno = self.get_object()
        usuarios = Usuario.objects.filter(turno = turno)
        serializer = UsuarioResumeSerializer(usuarios, many=True)
        return Response(serializer.data)
    

class FichajeViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Fichaje.objects.all()
        serializer = FichajeSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk=None):
        try:
            fichaje = Fichaje.objects.get(pk=pk)
            serializer = FichajeSerializer(fichaje)
            return Response(serializer.data)
        except Fichaje.DoesNotExist:
            return Response({"error": "Fichaje no encontrado"}, status=404)
        
        
    def create(self, request):
        serializer = FichajeSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # It is unnecessary update it
    #def update(self, request, pk=None):
    #    try:
    #        fichaje = Fichaje.objects.get(pk=pk)
    #        serializer = FichajeSerializer(fichaje, request.data)
    #        if(serializer.is_valid()):
    #            serializer.save()
    #            return Response(serializer.data)
    #        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #    except Fichaje.DoesNotExist:
    #        return Response({"error": "Fichaje no encontrado"}, status=404)
        

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
        
        
    def create(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if ( serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def update(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=404)
        
        serializer = UsuarioSerializer(user, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def destroy(self, request, pk=None):
        try:
            user = User.objects.get(pk = pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=404)
        
