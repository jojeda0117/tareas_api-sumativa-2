from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Tarea

class TareaAPITestCase(TestCase):
    """
    Clase para realizar pruebas unitarias a la API de Tareas.
    """

    def setUp(self):
        """
        Configuración inicial para cada prueba.
        Crea un usuario de prueba y un cliente API.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.admin_user = User.objects.create_superuser(username='adminuser', password='adminpassword')
        self.client = APIClient() # Cliente API para hacer solicitudes HTTP

    def test_authenticated_user_can_create_task(self):
        """
        Verifica que un usuario autenticado puede crear una tarea.
        """
        # Autenticar el cliente con el usuario de prueba
        response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        access_token = response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        # Datos para la nueva tarea
        data = {
            'titulo': 'Tarea de prueba autenticada',
            'descripcion': 'Esta es una descripción de prueba.',
            'completado': False
        }
        # Realizar la solicitud POST para crear la tarea
        response = self.client.post('/api/tareas/', data, format='json')

        # Verificar que la tarea se creó correctamente (código 201 Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Verificar que la tarea existe en la base de datos y está asignada al usuario
        self.assertEqual(Tarea.objects.count(), 1)
        tarea = Tarea.objects.get(id=response.json()['id'])
        self.assertEqual(tarea.titulo, 'Tarea de prueba autenticada')
        self.assertEqual(tarea.owner, self.user)

    def test_unauthenticated_user_cannot_create_task(self):
        """
        Verifica que un usuario NO autenticado NO puede crear una tarea.
        """
        # Asegurarse de que el cliente no está autenticado
        self.client.credentials() # Limpia cualquier credencial anterior

        # Datos para la nueva tarea
        data = {
            'titulo': 'Tarea de prueba no autenticada',
            'descripcion': 'Esta tarea debería fallar.',
            'completado': False
        }
        # Realizar la solicitud POST sin autenticación
        response = self.client.post('/api/tareas/', data, format='json')

        # Verificar que la solicitud fue rechazada con 401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # Verificar que no se creó ninguna tarea en la base de datos
        self.assertEqual(Tarea.objects.count(), 0)

    def test_authenticated_user_can_list_own_tasks(self):
        """
        Verifica que un usuario autenticado solo puede listar sus propias tareas.
        """
        # Crear algunas tareas para diferentes usuarios
        user2 = User.objects.create_user(username='testuser2', password='testpassword2')
        Tarea.objects.create(titulo='Tarea de testuser', owner=self.user, completado=False)
        Tarea.objects.create(titulo='Tarea de testuser2', owner=user2, completado=False)

        # Autenticar el cliente con el primer usuario de prueba
        response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'testpassword'})
        access_token = response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        # Realizar la solicitud GET para listar tareas
        response = self.client.get('/api/tareas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verificar que solo se muestra la tarea del usuario autenticado
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['owner'], 'testuser')

    def test_superuser_can_list_all_tasks(self):
        """
        Verifica que un superusuario puede listar todas las tareas.
        """
        # Crear algunas tareas para diferentes usuarios
        user2 = User.objects.create_user(username='testuser2', password='testpassword2')
        Tarea.objects.create(titulo='Tarea de testuser', owner=self.user, completado=False)
        Tarea.objects.create(titulo='Tarea de testuser2', owner=user2, completado=False)

        # Autenticar el cliente con el superusuario
        response = self.client.post('/api/token/', {'username': 'adminuser', 'password': 'adminpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        access_token = response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        # Realizar la solicitud GET para listar tareas
        response = self.client.get('/api/tareas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verificar que se muestran todas las tareas
        self.assertEqual(len(response.json()), 2)