from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters # Importamos filters para la paginación de búsqueda
from django_filters.rest_framework import DjangoFilterBackend # Importamos DjangoFilterBackend
from .models import Tarea
from .serializers import TareaSerializer

# ViewSet para manejar todas las operaciones CRUD del modelo Tarea
class TareaViewSet(viewsets.ModelViewSet):
    """
    API ViewSet para listar, crear, recuperar, actualizar y eliminar tareas.
    Permisos: Solo usuarios autenticados pueden acceder.
    Filtros: Permite filtrar por 'completado' y buscar por 'titulo' o 'descripcion'.
    Paginación: Implementada automáticamente por REST Framework.
    """
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Configuración de filtros
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['completado'] # Permite filtrar tareas por el campo 'completado'
    search_fields = ['titulo', 'descripcion'] # Permite buscar por 'titulo' o 'descripcion'
    ordering_fields = ['titulo', 'completado'] # Permite ordenar por 'titulo' o 'completado'

    # Configuración de paginación (automáticamente provista por REST Framework)
    # Por defecto, REST Framework usa una paginación simple.
    # Para configurar una paginación específica, puedes añadir:
    # pagination_class = YourCustomPaginationClass (si defines una)

    def perform_create(self, serializer):
        """
        Asigna el propietario (owner) de la tarea al usuario que realiza la solicitud.
        """
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Asegura que un usuario solo pueda ver sus propias tareas,
        a menos que sea un superusuario.
        """
        if self.request.user.is_superuser:
            return Tarea.objects.all()
        return Tarea.objects.filter(owner=self.request.user)
