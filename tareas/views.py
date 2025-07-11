from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Tarea
from .serializers import TareaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    """
    Conjunto de Vistas (ViewSet) para gestionar las tareas en la API.

    Proporciona operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
    para el modelo Tarea.

    - **Listar Tareas (GET /api/tareas/):**
        Retorna una lista de todas las tareas del usuario autenticado.
        Los superusuarios pueden ver todas las tareas.
        Permite filtrar, buscar y ordenar.
    - **Crear Tarea (POST /api/tareas/):**
        Crea una nueva tarea asignándola automáticamente al usuario autenticado.
    - **Obtener Detalle de Tarea (GET /api/tareas/{id}/):**
        Retorna los detalles de una tarea específica del usuario autenticado.
    - **Actualizar Tarea (PUT/PATCH /api/tareas/{id}/):**
        Actualiza una tarea existente del usuario autenticado.
    - **Eliminar Tarea (DELETE /api/tareas/{id}/):**
        Elimina una tarea del usuario autenticado.

    **Permisos:**
    Requiere autenticación JWT. Solo usuarios autenticados pueden acceder.

    **Filtros:**
    - `completado`: `true` o `false` (ej. `?completado=true`)
    **Búsqueda:**
    - `search`: Texto para buscar en `titulo` o `descripcion` (ej. `?search=comprar`)
    **Ordenamiento:**
    - `ordering`: Campo por el cual ordenar (`titulo`, `completado`).
      Usa `-` para orden descendente (ej. `?ordering=-titulo`)
    """
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['completado']
    search_fields = ['titulo', 'descripcion']
    ordering_fields = ['titulo', 'completado']

    def perform_create(self, serializer):
        """
        Crea una nueva instancia de Tarea y asigna el usuario autenticado como su propietario.
        """
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Retorna el queryset de tareas, filtrando por el usuario autenticado.
        Los superusuarios pueden ver todas las tareas.
        """
        if self.request.user.is_superuser:
            return Tarea.objects.all()
        return Tarea.objects.filter(owner=self.request.user)