from rest_framework import serializers
from .models import Tarea
from django.contrib.auth.models import User

class TareaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Tarea.

    Convierte instancias del modelo Tarea en representaciones JSON
    y viceversa. Incluye el nombre de usuario del propietario de la tarea.

    **Campos:**
    - `id`: Identificador único de la tarea (solo lectura).
    - `titulo`: Título de la tarea (cadena de texto).
    - `descripcion`: Descripción detallada de la tarea (texto, opcional).
    - `completado`: Estado de la tarea (booleano, `true` si está completada, `false` si no).
    - `owner`: Nombre de usuario del propietario de la tarea (solo lectura).
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'descripcion', 'completado', 'owner']
