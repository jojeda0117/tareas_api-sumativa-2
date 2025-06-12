from rest_framework import serializers
from .models import Tarea

# Define el serializador para el modelo Tarea
class TareaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Tarea.
    Convierte instancias del modelo Tarea en datos JSON y viceversa.
    """
    class Meta:
        model = Tarea # El modelo al que se asocia este serializador
        fields = '__all__' # Incluye todos los campos del modelo en el serializador
