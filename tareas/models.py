from django.db import models 

# Define el modelo Tarea
class Tarea(models.Model):
    """
    Modelo para representar una tarea en la lista ToDo.
    """
    titulo = models.CharField(max_length=200) # Título de la tarea
    descripcion = models.TextField(blank=True, null=True) # Descripción detallada de la tarea (opcional)
    completado = models.BooleanField(default=False) # Indica si la tarea ha sido completada

    class Meta:
        # Ordena las tareas por título por defecto
        ordering = ['titulo']

    def __str__(self):
        """
        Representación de cadena del objeto Tarea.
        """
        return self.titulo
