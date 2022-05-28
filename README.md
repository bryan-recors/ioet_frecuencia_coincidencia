# Frecuencia con la que coinciden los empleados en una empresa con horario flexible
La empresa ACME ofrece a sus empleados la flexibilidad de trabajar las horas que deseen. Pero debido a algunas circunstancias externas, necesitan saber qué empleados han estado en la oficina en el mismo período de tiempo, generar una tabla que contenga pares de empleados y la frecuencia con la que han coincidido en la oficina.

# solución
Se desarrolló un programa de consola que permite indicar la dirección de un archivo.txt donde debe estar los registros que se desea analizar, los datos debes ser correctos ya que se valida su estructura.
Los días de la semana se deben indicar de la siguiente manera: MO,TU,WE,TH,FR,SA,SU
ejemplo de un registro: ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
el archivo debe contener por lo menos 5 registros.

# Instalación
-clonar el proyecto, crear un entorno virtual
-activar el entorno virtual 
-instalar las librerías que se encuentran en el archivo requirements.txt
-ejecutar el proyecto desde el archivo main.py (python main.py)

# Uso
-proporcionar la dirección del archivo txt que se desea analizar 
-si el archivo se encuentra fuera de la carpeta del proyecto ingrese la ruta absoluta del archivo
-ejemplo: /Usuarios/bryan/Desktop/horarios.txt
-si el archivo lo copia dentro de la carpeta del proyecto puede usar la ruta relativa 
-si no proporciona la ruta del archivo s mostrará los resultados del archivo de horarios.txt
-posteriormente se mostraran los resultados de los pares de empleados y la frecuencia con la que coinciden en la oficina

# Arquitectura
-use la arquitectura mvc para desarrollar la solución, 
model.py. define las funciones para cargar y validar los datos.
controllerpy: define las funciones para obtener los pares y frecuencias 
view.py: define las funciones para solicitar la rta del archivo y mostrar los resultados 

# Pruebas
Las pruebas desarrolladas se encuentran en el archivo test_frecuencias.py para correr las pruebas dentro del entorno virtual ejecutar pytest
