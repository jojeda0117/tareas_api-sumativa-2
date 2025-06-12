from django.contrib import admin
from .models import Tarea # Esta importación SÍ es correcta en admin.py

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'completado')
    list_filter = ('completado',)
    search_fields = ('titulo', 'descripcion')