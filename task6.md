# Vistas relacionadas

Crear dos vistas simples para jugadores, vista de arbol y formulario.
Pasar esas vistas por contexto en el equipo.
Darle prioridad 100 para que no rompa las vistas normales de jugadores.

# Opciones m2o

En Incidencias no se debe de poder acceder al usuario ni crear usuarios nuevos de manera rápida, pero si desde vista de formulario.
En las etiquetas de las incidencias no se debe de poder crear ninguna etiqueta.

# Modelo nuevo actividades a realizar

Vamos a crear por una parte un modelo nuevo llamado actividades a realizar. Este modelo va a ser un one2many para las incidencias.

Va a tener un campo nombre y un campo estado (Sin hacer, en curso y hecho)

# Vista embembida

Vamos a añadir este modelo como vista embebida en incidencias

# Contexto

Vamos a decir desde contexto, que el campo por defecto sea sin hacer
