from rest_framework import serializers
from .models import Tarea
from django.contrib.auth.models import User # Importamos el modelo User

# Serializador para el modelo Tarea
class TareaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Tarea, incluyendo el propietario (owner).
    """
    # Campo de solo lectura para el nombre de usuario del propietario
    # source='owner.username' accede al campo username del objeto User relacionado
    # read_only=True asegura que este campo no se use para la creación/actualización
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'descripcion', 'completado', 'owner'] # Asegúrate de incluir 'owner'
        # read_only_fields = ['owner'] # Alternativa si no usas ReadOnlyField

