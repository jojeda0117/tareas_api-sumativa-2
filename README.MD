Proyecto Django REST API para Gestión de Tareas (ToDo List)
Este proyecto implementa una API REST para la gestión de tareas con funcionalidades avanzadas, incluyendo autenticación JWT, relación de tareas con usuarios, operaciones CRUD completas, filtrado, búsqueda y ordenamiento.

Tabla de Contenidos
Requisitos

Instalación

Configuración de la Base de Datos

Creación de Superusuario

Ejecutar el Servidor

Uso de la API (Endpoints)

Autenticación JWT

Gestión de Tareas (CRUD)

Filtros, Búsqueda y Ordenamiento

Acceder al Panel de Administración

Pruebas Unitarias

Requisitos
Python 3.x

pip (gestor de paquetes de Python)

Instalación
Clona este repositorio:

git clone https://github.com/tu-usuario-de-github/tareas_api.git
cd tareas_api

(Nota: Reemplaza tu-usuario-de-github con tu nombre de usuario de GitHub real y tareas_api con el nombre de tu repositorio si es diferente.)

Crea un entorno virtual (opcional pero recomendado):

python -m venv venv
source venv/bin/activate  # En Linux/macOS
# venv\Scripts\activate   # En Windows

Instala las dependencias:

pip install django djangorestframework djangorestframework-simplejwt django-filter

(O si tienes un requirements.txt actualizado, usa pip install -r requirements.txt)

Configuración de la Base de Datos
Después de instalar las dependencias, aplica las migraciones para crear las tablas de la base de datos (incluyendo el nuevo campo owner en el modelo Tarea):

python manage.py makemigrations tareas
python manage.py migrate

Creación de Superusuario
Para acceder al panel de administración y para pruebas de autenticación, crea un superusuario:

python manage.py createsuperuser

Sigue las indicaciones para crear un nombre de usuario y una contraseña.

Ejecutar el Servidor
Para iniciar el servidor de desarrollo de Django:

python manage.py runserver

El API estará disponible en http://127.0.0.1:8000/api/.

Uso de la API (Endpoints)
Todas las rutas de gestión de tareas están protegidas y requieren autenticación JWT.

Autenticación JWT
Para interactuar con la API, primero debes obtener un token de acceso.

1. Obtener Token (POST)
URL: http://127.0.0.1:8000/api/token/

Headers:

Content-Type: application/json

Body (raw, JSON):

{
    "username": "tu_usuario",
    "password": "tu_contraseña"
}

Respuesta Exitosa (200 OK):

{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}

Guarda el token access.

2. Refrescar Token (POST)
Cuando tu token de acceso caduque, puedes usar el token de refresco para obtener uno nuevo.

URL: http://127.0.0.1:8000/api/token/refresh/

Headers:

Content-Type: application/json

Body (raw, JSON):

{
    "refresh": "tu_token_de_refresco"
}

Respuesta Exitosa (200 OK):

{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}

Gestión de Tareas (CRUD)
Todas las solicitudes a los endpoints de tareas deben incluir el encabezado Authorization con tu token de acceso:

Key: Authorization

Value: Bearer TU_TOKEN_DE_ACCESO

1. Listar Tareas (GET)
Muestra las tareas del usuario autenticado (o todas si es superusuario).

URL: http://127.0.0.1:8000/api/tareas/

Respuesta Exitosa (200 OK): Array de objetos Tarea. Cada tarea incluirá el campo "owner".

2. Crear Tarea (POST)
El owner de la tarea se asignará automáticamente al usuario que realiza la solicitud.

URL: http://127.0.0.1:8000/api/tareas/

Headers: Content-Type: application/json

Body (raw, JSON):

{
    "titulo": "Mi nueva tarea",
    "descripcion": "Descripción detallada de la tarea.",
    "completado": false
}

Respuesta Exitosa (201 Created): Objeto Tarea con el id asignado y owner.

3. Obtener Detalle de Tarea (GET /{id}/)
URL: http://127.0.0.1:8000/api/tareas/{id}/

Respuesta Exitosa (200 OK): Objeto Tarea específica.

4. Actualizar Tarea (PUT / PATCH /{id}/)
URL: http://127.0.0.1:8000/api/tareas/{id}/

Headers: Content-Type: application/json

Body (raw, JSON) - Ejemplo PATCH:

{
    "completado": true
}

Respuesta Exitosa (200 OK): Objeto Tarea actualizado.

5. Eliminar Tarea (DELETE /{id}/)
URL: http://127.0.0.1:8000/api/tareas/{id}/

Respuesta Exitosa (204 No Content).

Filtros, Búsqueda y Ordenamiento
Puedes combinar estos parámetros en la URL de las solicitudes GET /api/tareas/.

Filtrar por estado de completado: ?completado=true o ?completado=false

Ejemplo: http://127.0.0.1:8000/api/tareas/?completado=true

Buscar por título o descripción: ?search=tu_palabra_clave

Ejemplo: http://127.0.0.1:8000/api/tareas/?search=cafe

Ordenar resultados: ?ordering=campo (ascendente) o ?ordering=-campo (descendente)

Campos disponibles: titulo, completado

Ejemplo: http://127.0.0.1:8000/api/tareas/?ordering=-titulo

Combinar parámetros:

Ejemplo: http://127.0.0.1:8000/api/tareas/?completado=false&search=compras&ordering=titulo

Acceder al Panel de Administración
Para gestionar las tareas y usuarios a través de una interfaz gráfica:

URL: http://127.0.0.1:8000/admin/

Utiliza las credenciales del superusuario que creaste.

Pruebas Unitarias
Para ejecutar las pruebas unitarias y verificar el correcto funcionamiento de la API, asegúrate de tener tu entorno virtual activado y ejecuta el siguiente comando en la raíz del proyecto:

python manage.py test tareas