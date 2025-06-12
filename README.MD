Proyecto Django REST API para Gestión de Tareas (ToDo List)
Este proyecto fue realizado por Juan Ojeda 29502693

Tabla de Contenidos

Requisitos

Instalación

Configuración de la Base de Datos

Ejecutar el Servidor

Uso de la API

Acceder al Panel de Administración

Requisitos
Python 3.x

pip (gestor de paquetes de Python)

Instalación
Clona este repositorio:

git clone https://github.com/jojeda0117/tareas_api.git
cd tareas_api


entorno virtual 

python -m venv venv
source venv/bin/activate  # En Linux/macOS
# venv\Scripts\activate   # En Windows

Instala las dependencias:

pip install -r requirements.txt

(Si aún no tienes requirements.txt, puedes crearlo después de instalar las dependencias con pip freeze > requirements.txt)
O instala manualmente:

pip install django djangorestframework

Configuración de la Base de Datos
Después de instalar las dependencias, necesitas aplicar las migraciones para crear las tablas de la base de datos:

python manage.py makemigrations tareas
python manage.py migrate

Ejecutar el Servidor
Para iniciar el servidor de desarrollo de Django:

python manage.py runserver

El API estará disponible en http://127.0.0.1:8000/api/tareas/.

Uso de la API
Puedes usar herramientas como Postman, Insomnia o curl para interactuar con la API.

Endpoints Disponibles
Listar y Crear Tareas:

URL: http://127.0.0.1:8000/api/tareas/

Métodos Permitidos: GET, POST

Ejemplos con Postman
1. Obtener todas las tareas (GET)
Método: GET

URL: http://127.0.0.1:8000/api/tareas/

2. Crear una nueva tarea (POST)
Método: POST

URL: http://127.0.0.1:8000/api/tareas/

Headers:

Content-Type: application/json

Body (raw, JSON):

{
    "titulo": "Compras",
    "descripcion": "Leche, pan, huevos, frutas",
    "completado": false
}

(Puedes omitir completado o establecerlo en true)

Acceder al Panel de Administración
Para acceder al panel de administración de Django y gestionar las tareas a través de una interfaz gráfica, primero necesitas crear un superusuario:

python manage.py createsuperuser

Sigue las indicaciones para crear un nombre de usuario y una contraseña.

Una vez creado, puedes acceder al panel de administración en: http://127.0.0.1:8000/admin/
Utiliza las credenciales que creaste.