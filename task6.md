# Vistas relacionadas

Crear dos vistas simples para jugadores, vista de arbol y formulario.
Pasar esas vistas por contexto en el equipo.
Darle prioridad 100 para que no rompa las vistas normales de jugadores.

# Opciones m2o

En Incidencias no se debe de poder acceder al usuario ni crear usuarios nuevos de manera rápida, pero si desde vista de formulario.
En las etiquetas de las incidencias no se debe de poder crear ninguna etiqueta.

# Modelo nuevo acciones a realizar

Vamos a crear por una parte un modelo nuevo llamado acciones a realizar. Este modelo va a ser un one2many para las incidencias.

Va a tener un campo nombre y un campo estado (Borrador, abierto y hecho) // Igual que en incidencias

# Vista embembida

Vamos a añadir este modelo como vista embebida en incidencias

# Contexto

Vamos a decir desde contexto, que el campo por defecto sea el mismo que la incidencia

# Dominio

Añadimos un campo boolean de disponible a la clínica
Hacemos un dominio en la incidencia que filtre las clínicas que están disponibles
