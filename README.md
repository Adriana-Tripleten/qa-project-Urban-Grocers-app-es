         APLICACIÓN URBAN GROCERS
# Pruebas Automatizadas con Pytest. Sprint 7: Este proyecto contiene pruebas automatizadas en Python para verificar el funcionamiento de la API de creación de kits personalizados para usuarios/as.

## 📁 Estructura del proyecto: El proyecto contiene los siguientes 6 archivos:
	- `configuration.py`: Contiene la URL y rutas de solicitud. 
	- `data.py`: Contiene los datos necesarios para crear usuarios/as y kits. Entonces, van los cuerpos (BODY) y diccionarios de la solicitud POST (create user, create kit y headers).
	- `sender_stand_request.py`: Módulo encargado de enviar solicitudes HTTP a la API. Aquí se incluye, la función para crear un nuevo usuario/a, función para crear un kit (post_new_client_kit). La función post_new_client_kit recibe  dos parámetros (kit body y auth_token).
	- `create_kit_name_kit_test.py`: Contiene pruebas para validar el comportamiento del nombre del kit, es decir, aquí encontrarán la lista de comprobación. Las pruebas aquí agregadas contienen un positive_assert(kit_body) y un negative_assert_code_400 (kit_body) 
	- `README.md`: Es un archivo de texto, donde se describe el proyecto que ayudará a los colaboradores a entender cómo usarlo.
	- `.gitignore`: Está configurado para excluir archivos innecesarios. 


### 🚀 Cómo ejecutar las pruebas

	 1. Verifica que tienes Python instalado.
	 2. Instala los paquetes pytest y request para ejecutar las pruebas: Para ello puede buscarlas e instalarlas desde Python Packages. 
	 3. Ejecuta todas las pruebas con el comando pytest -v ó si usa py en Windows se debe emplear como comando py -m pytest -v.
