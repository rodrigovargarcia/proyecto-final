# proyecto-final
Mi proyecto final

Tenemos 3 tipos de modelos: Familiar
                            Mascota
                            Automovil

cada uno de ellos con sus correspondientes funcionalidades heredadas de Django
mediante los paths podemos ver la lista de datos ingresados, con sus caracteristicas, asi como también 
podemos ver en detalle cada uno de ellos, eliminarlos y actualizarlos.

creamos cada uno de los modelos en la carpeta models.py y luego realizamos las migrations para poder continuar.
luego con cada funcionalidad que querramos incorporar, seguimos el workflow de django, configurando o creando templates, 
los cuales permiten mostrar la informacion al usuario, siguiendo por las views que cargan los datos provenientes del modelo y por ultimo
configuramos las rutas o paths necesarias para poder realizar cada funcion.
tambien, creamos la carpeta seed_data que nos permite cargar informacion en la base de datos para poder testear el funcionamiento correcto de nuestro MVT

