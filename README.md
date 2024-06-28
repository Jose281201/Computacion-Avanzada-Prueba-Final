README: Tienda (Aplicación de Gestión de Tienda)
Introducción

Tienda es una aplicación de interfaz gráfica de usuario (GUI) basada en Python
diseñada para facilitar la gestión de información de productos dentro de una tienda. Utiliza una
base de datos MySQL para almacenar y recuperar datos de productos, permitiendo a los
administradores de la tienda agregar, actualizar, eliminar y ver detalles de productos de manera
eficiente.
Características
● GUI Intuitiva: Interfaz fácil de usar construida con Tkinter, proporcionando un diseño
visual claro para administrar la información del producto.
● Integración con MySQL: Se conecta sin problemas a una base de datos MySQL
llamada "tienda" para almacenar y recuperar registros de productos.
● Operaciones CRUD:
○ Crear: Agrega fácilmente nuevos productos a la base de datos con su nombre,
marca, tamaño y precio.
○ Leer: Muestra una lista completa de todos los productos en formato de tabla,
incluyendo su ID, nombre, marca, tamaño y precio.
○ Actualizar: Modifica el precio de un producto existente ingresando su nombre y el
nuevo precio.
○ Eliminar: Elimina productos de la base de datos especificando su nombre.
● Validación: Validación básica de entrada para evitar la entrada de datos no válidos (por
ejemplo, campos vacíos).
● Retroalimentación: Proporciona mensajes informativos al usuario sobre el éxito o
fracaso de las operaciones de la base de datos.
Cómo Funciona
1. Conexión a la Base de Datos: La aplicación establece una conexión a tu base de datos
MySQL local (asegúrate de que esté en ejecución y de que tengas las credenciales
correctas).
2. Interacción con la GUI:
○ Se proporcionan campos de entrada para ingresar los detalles del producto.
○ Los botones activan acciones como "Nuevo +", "Guardar", "Eliminar", "Listar" y
"Actualizar".
○ Una tabla muestra la información del producto obtenida de la base de datos.
3. Operaciones de la Base de Datos:
○ Al hacer clic en el botón "Guardar", se inserta un nuevo registro de producto en la
base de datos.
○ El botón "Actualizar" modifica el precio de un producto existente.
○ "Eliminar" quita un producto de la base de datos.
○ "Listar" obtiene y muestra todos los datos del producto en la tabla.
4. Retroalimentación del Usuario: Los cuadros de mensaje informan al usuario sobre los
resultados de las acciones (por ejemplo, "Registro Guardado", "Registro Eliminado").
Requisitos Previos
● Python: Python 3.x instalado en tu sistema.
● MySQL: Un servidor MySQL en ejecución con una base de datos llamada "tienda" y una
tabla llamada "articulos" (consulta a continuación la estructura de la tabla).
● Tkinter: Biblioteca GUI Tkinter instalada (generalmente incluida con Python).
● PyMySQL: Biblioteca para interactuar con bases de datos MySQL (instala usando pip
install PyMySQL).
Estructura de la Tabla de la Base de Datos
La tabla "articulos" en tu base de datos MySQL debe tener las siguientes columnas:
Nombre de Columna Tipo de Dato
ID INT (auto-increment)
nombre VARCHAR(255)
marca VARCHAR(255)
tamaño VARCHAR(255)
precio DECIMAL(10, 2)
Cómo Ejecutar
1. Configuración: Asegúrate de tener MySQL en ejecución con la base de datos "tienda" y
la tabla "articulos" creada como se describe anteriormente.
2. Instalar Dependencias: Ejecuta pip install PyMySQL en tu terminal para instalar la
biblioteca necesaria.
3. Ejecutar: Guarda el código proporcionado como un archivo Python (por ejemplo,
admin_tienda.py) y ejecútalo desde tu terminal usando python admin_tienda.py.
Notas Adicionales
● Manejo de Errores: Considera agregar un manejo de errores más robusto para detectar
posibles problemas de conexión a la base de datos o escenarios de entrada no válidos.
● Seguridad: Para entornos de producción, implementa medidas de seguridad para
proteger las credenciales de la base de datos y prevenir el acceso no autorizado.