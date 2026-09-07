Pruebas Automatizadas de API: Creación de Kits en Urban Grocers
Este proyecto contiene una suite de pruebas automatizadas para la API de Urban Grocers. Su propósito es validar el comportamiento de la ruta de creación de kits de usuarios, verificando la integración entre la autenticación, la estructura de las peticiones y las respuestas del servidor.

Estructura del Proyecto
configuration.py: Define la URL base del servidor y las rutas (endpoints) utilizadas por la API.

data.py: Contiene los diccionarios con la estructura de datos para el cuerpo de las peticiones (user_body, kit_body) y los encabezados HTTP.

sender_stand_request.py: Mantiene la lógica para enviar peticiones HTTP POST a la API utilizando la librería requests.

create_kit_name_kit_test.py: Archivo principal de pruebas. Contiene las funciones auxiliares (positive_assert, negative_assert) y los casos de prueba ejecutados con pytest.

Requisitos Previos
Python 3.10 o superior.

Entorno virtual de Python (.venv).

Librerías requests y pytest.

Instalación y Configuración
Clona el repositorio en tu máquina local.

Activa tu entorno virtual:

Windows: .venv\Scripts\activate

macOS/Linux: source .venv/bin/activate

Instala las dependencias necesarias:
pip install requests pytest

Ejecución de las Pruebas

Para ejecutar todos los casos de prueba y visualizar las salidas de consola:
pytest create_kit_name_kit_test.py

Cobertura de Casos de Prueba
Pruebas Positivas (Código 201 Created)
Nombre por defecto: Creación de kit utilizando los valores base definidos en data.py.

Límites válidos: Validación con nombres de 1 carácter y dentro del rango máximo permitido.

Formatos aceptados: Nombres con caracteres especiales, espacios y tipos de texto variados.

Pruebas Negativas (Código 400 Bad Request)
Cadena vacía: Intento de creación enviando "" en el campo name.

Exceso de caracteres: Nombres que sobrepasan la longitud máxima definida por las reglas de negocio.

Tipos de datos inválidos: Envío de valores numéricos o ausencia de parámetros requeridos.

