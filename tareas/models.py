from django.db import models
from django.contrib.auth.models import User # Importamos el modelo User predeterminado de Django

# Define el modelo Tarea
class Tarea(models.Model):
    """
    Modelo para representar una tarea en la lista ToDo.
    """
    titulo = models.CharField(max_length=200) # Título de la tarea
    descripcion = models.TextField(blank=True, null=True) # Descripción detallada de la tarea (opcional)
    completado = models.BooleanField(default=False) # Indica si la tarea ha sido completada
    # Añadimos un campo ForeignKey para relacionar la tarea con un usuario (owner)
    # on_delete=models.CASCADE significa que si el usuario se elimina, sus tareas también se eliminarán.
    # related_name='tareas' permite acceder a las tareas de un usuario como user.tareas.all()
    owner = models.ForeignKey(User, related_name='tareas', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        # Ordena las tareas por título por defecto
        ordering = ['titulo']

    def __str__(self):
        """
        Representación de cadena del objeto Tarea.
        """
        return self.titulo
