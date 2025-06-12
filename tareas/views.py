from rest_framework import generics
from .models import Tarea
from .serializers import TareaSerializer

# Vista para listar tareas y crear nuevas tareas
class TareaListCreateView(generics.ListCreateAPIView):
    """
    API View para listar todas las tareas y crear nuevas tareas.
    - GET: Retorna una lista de todas las tareas existentes.
    - POST: Permite crear una nueva tarea.
    """
    queryset = Tarea.objects.all() # Consulta todas las tareas
    serializer_class = TareaSerializer # Utiliza TareaSerializer para la serialización
