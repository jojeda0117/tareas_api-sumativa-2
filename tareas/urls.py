from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from .views import TareaViewSet 

# Crea una instancia del router
router = DefaultRouter()
# Registra el ViewSet con el router.
# 'tareas' será el prefijo de URL para todas las rutas generadas por TareaViewSet.
router.register(r'tareas', TareaViewSet)

urlpatterns = [
    # Incluye las URLs generadas automáticamente por el router.
    # Esto creará rutas como /api/tareas/ (GET, POST), /api/tareas/{id}/ (GET, PUT, PATCH, DELETE)
    path('', include(router.urls)),
]
