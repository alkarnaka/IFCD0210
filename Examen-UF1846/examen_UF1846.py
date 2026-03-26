#1.  Dado el siguiente sistema: 
    #●  Un navegador muestra una web 
    #●  Un servidor procesa peticiones 
    #●  Una base de datos almacena usuarios 


#Responde: 
#1.  ¿Qué parte es el frontend? 

#    La parte de una aplicación que interactúa con el usuario, en este caso el navegador. 

#2.  ¿Qué parte es el backend? 

#    La parte de una aplicación que maneja la lógica de negocio y se comunica con la base de datos, en este caso el servidor. 

#3.  ¿Es una arquitectura distribuida? ¿Por qué? 

#    Sí, porque el frontend y el backend están separados y pueden estar en diferentes servidores o ubicaciones.


#2.  Tienes esta API: 

#GET    /usuarios 
#POST    /usuarios 
#GET    /usuarios/5 
#DELETE   /usuarios/5 
#Responde: 

#1.  ¿Qué hace cada endpoint? 

#GET /usuarios: Obtiene una lista de todos los usuarios.
#POST /usuarios: Crea un nuevo usuario.
#GET /usuarios/5: Obtiene los detalles del usuario con ID 5.
#DELETE /usuarios/5: Elimina el usuario con ID 5.

#2.  ¿Cuál usarías para crear un usuario? 

#    POST /usuarios

#3.  ¿Cuál usarías para eliminarlo? 

#    DELETE /usuarios/5


#3. Diseña una API para una aplicación de tareas (to-do list). 
#Define al menos 4 endpoints: 

#●  Obtener tareas 

# GET/tareas

#●  Crear tarea 

# POST/tareas

#●  Actualizar tarea

# PUT/tareas/<int:id>

#●  Eliminar tarea 

# DELETE/tareas/<int:id>

#4. Dada esta respuesta de una API: 
#{ 
# "id": 1, 
# "nombre": "Juan", 
# "email": "juan@email.com", 
# "activo": true 
#} 

#Responde: 
#1.  ¿Qué tipo de formato es este? 

#    JSON (JavaScript Object Notation)

#2.  ¿Qué valor tiene "nombre"? 

#    "Juan"

#3.  ¿El usuario está activo? 

#    Sí, porque "activo" tiene el valor true.

#4.  ¿Qué tipo de dato es "activo"? 

#    Booleano (boolean)

# 
#5. Ordena correctamente estos pasos: 

#1.  El servidor consulta la base de datos 
#2.  El navegador muestra los datos 
#3.  El usuario hace una petición 
#4.  El servidor envía una respuesta 
##Escribe el orden correcto (1 → 4)

#    3 → 1 → 4 → 2