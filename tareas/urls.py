from django.urls import path
from .views import TareaListCreateView

urlpatterns = [
    # Define una URL para la vista de listar y crear tareas
    # La ruta es 'tareas/' y utiliza la vista TareaListCreateView
    path('tareas/', TareaListCreateView.as_view(), name='tarea-list-create'),
]
