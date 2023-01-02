# Link a video de presentación en Youtube: 

----

> https://www.youtube.com/watch?v=sJ4p-Rp7y7o


# Introduccion
                
----

En este repositorio vamos a crear 3 diferentes tipos de modelos, utilizando el framework Django y sus correspondientes funcionalidades, las cuales nos van a permitir crear distintos paths o rutas facilitando el acceso a las caracteristicas de cada uno de los modelos, asi como también, poder eliminar, actualizar o crear nuevos datos.

### Programas necesarios
Debemos tener instalado VSCode, git y Django en nuestro ordenador.

### Una vez instalados, continuar con la siguiente serie de pasos:
                
- Abrir el editor de código VSCode.
- Ingresar a con su usuario a: 

>http://github.com

- Para clonar el repositorio debemos seleccionar Clone git repository y copiar la dirección URL del proyecto

- Abrir o crear una carpeta en la cual vamos a trabajar desde nuestro editor.

- Una vez clonado el repositorio en nuestro ordenador, ejecutar el siguiente comando en la terminal de VSCode:

 `python manage.py runserver`

>Este comando permite poner a funcionar el programa en nuestro servidor local.

- Ingresamos a para corroborar que se encuentre funcionando correctamente: 

> http://localhost:8000/

### Modelos
- En la web encontramos 3 distintos tipos de modelos: 

>panel-familia 
panel-automoviles 
panel-mascotas

- Agrega al final de la URL de nuestro servidor local los nombres de los modelos mencionados anteriormente para poder visualizar los datos cargados en cada uno de ellos. 

 ###### Ejemplo
>http://127.0.0.1:8000/panel-familia : Para ver los familiares

- En caso de querer crear un nuevo familiar:
 ###### Ejemplo
>http://127.0.0.1:8000/panel-familia/crear Para crear un familiar nuevo 

- Para Buscar, debemos ingresar :

>http://127.0.0.1:8000/panel-familia/buscar Para buscar un familiar por nombre

- Reemplaza mi-familia por automoviles y mascotas respectivamente.

- Si quieres tener algunos datos precargados, en la terminal, ejecuta el comando:

 `python manage.py shell`

- Luego:

 `import seed_data`

                
