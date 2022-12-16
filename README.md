# proyecto-final
##Introducción
=============

En este repositorio vamos a crear 3 diferentes tipos de modelos, utilizando el framework Django y sus correspondientes funcionalidades, las cuales nos van a permitir crear distintos paths o rutas facilitando el acceso a las caracteristicas de cada uno de los modelos, asi como tambien, poder eliminar, actualizar o crear nuevos datos.

###Programas necesarios
Debemos tener instalado VSCode, git y Django en nuestro ordenador.

####Una vez corroborado tener instalados los programas anteriormente mencionados, seguir esta serie de pasos
                
1 Abrir VSCode.

2 Seleccionar Clone git repository y agregar la URL de este proyecto.

3 Seleccionar o crear una carpeta para el programa.

4 En la terminal ejecuta los comandos: python manage.py migrate python manage.py runserver

5 Ya se puede abrir la pagina que aparece en el texto, tipicamente: http://127.0.0.1:8000/

6 Si quieres tener algunos datos precargados, en la terminal, ejecuta los comandos: python manage.py shell import seed_data

En la web hay 3 tipos de modelos: mi-familia, automoviles y mascotas:

Agrega las url que ves abajo a la url en la barra de direcciones para utilizarlas, las funciones Alta y Buscar están funcionando, las demás no están aún 100% testeadas.
Ejemplos, reemplaza las URLs antes de mi-familia por las que te aparezcan cuando haces runserver! Familia

http://127.0.0.1:8000/mi-familia : Para ver los familiares(sólo veras Familiares pre cargados si hiciste el paso 6)

http://127.0.0.1:8000/mi-familia/alta Para crear un familiar nuevo

http://127.0.0.1:8000/mi-familia/buscar Para buscar un familiar por nombre

Reemplaza mi-familia por automoviles y mascotas respectivamente.
                
Muchas gracias!
