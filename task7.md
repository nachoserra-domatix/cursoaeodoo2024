# Vistas
* Vista kanban de equipos
* Filtro al escribir en jugadores de deporte y equipo
* Filtro de jugadores titulares
* Agrupación en jugadores de equipo y deporte y fecha de nacimiento
  
# Modelos nuevos

## Modelo de liga
* Nombre
* Fecha de inicio
* Fecha de fin
* Deporte
* Lineas de liga (o2m)

## Modelo de lineas de liga
* Equipo
* Puntuación

## Modelo de partidos
* Deporte (opciones de no poderse crear rápidamente el registro)
* Fecha de partido con hora incluida
* Equipo ganador
* Puntuación que se lleva al ganar(por defecto pongamos 3)
* Lineas de partidos (o2m)

## Modelo lineas de partidos
* Equipo
* Puntuación (que serán goles/canastas/etc)


# Vistas nuevos modelos
* Vistas embebidas para las líneas de liga y de partidos

# Dominios
* En las ligas, añadir dominio al equipo de las lineas para que solo encuentre equipos con el mismo deporte que la liga

# Vistas cont.
* Vista pivot, graph y calendario de los partidos

# Campos calculados
* En los partidos, se debe calcular el equipo ganador dependiendo de la puntuación de las lineas.
* En la liga, tiene que haber un botón que calcule las puntuaciones de todos los equipos
