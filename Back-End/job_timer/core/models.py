from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    ADMIN= 'admin'
    EMPLEADO = 'empleado'
    
    ROLES = [
        (ADMIN, 'Administrador'),
        (EMPLEADO, 'Empleado'),
    ]
    
    rol = models.CharField(max_length=10,choices=ROLES, default=EMPLEADO)
    departamento = models.ForeignKey('Departamento', on_delete= models.SET_NULL, null=True, blank=True)
    turno = models.ForeignKey('Turno', on_delete=models.SET_NULL, null=True, blank=True)



class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    
    
class Turno(models.Model):
    nombre =  models.CharField(max_length=100)
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()
    
    def __str__(self):
        return f"{self.nombre} ({self.hora_entrada} - {self.hora_salida})"
    
    
    
class Fichaje(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    hora_entrada = models.DateTimeField(null=True, blank=True)
    hora_salida = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Fichaje de {self.usuario.username} el {self.fecha}"