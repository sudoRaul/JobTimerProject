from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

# Al heredar de AbstractUser se incluyen campos como first_name, last_name, email, password
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
    descripcion = models.CharField(max_length=255, default="Departamento creado sin descripción")
    
    def __str__(self):
        return self.nombre
    
    
    
class Turno(models.Model):
    nombre =  models.CharField(max_length=100)
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()
    
    def __str__(self):
        return f"{self.nombre} ({self.hora_entrada} - {self.hora_salida})"
    
    
    
class Fichaje(models.Model):
    
    CHOICES = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida')
    ]
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=CHOICES)
    fecha = models.DateField(editable=False)
    hora = models.TimeField(editable=False)
    
    
    def save(self, *args, **kwargs):
        now = timezone.now()
        self.fecha = now.date()
        self.hora = now.time()
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return f"Fichaje de {self.usuario.username} el {self.fecha}"