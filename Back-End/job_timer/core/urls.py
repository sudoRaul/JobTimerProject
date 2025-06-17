from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, DepartamentoViewSet, TurnoViewSet, FichajeViewSet

router = DefaultRouter()

router.register(r'departamentos', DepartamentoViewSet)
router.register(r'turnos', TurnoViewSet)
router.register(r'fichajes', FichajeViewSet)
router.register(r'usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('api/', include(router.urls)),
]