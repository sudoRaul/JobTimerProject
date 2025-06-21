from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, DepartamentoViewSet, TurnoViewSet, FichajeViewSet

router = DefaultRouter()

router.register(r'departamentos', DepartamentoViewSet, basename='departamento')
router.register(r'turnos', TurnoViewSet, basename='turno')
router.register(r'fichajes', FichajeViewSet, basename='fichaje')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('api/', include(router.urls)),
]