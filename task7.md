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
* Deporte
* Fecha de partido con hora incluida
* Equipo ganador
* Puntuación que se lleva al ganar(por defecto
* Lineas de partidos (o2m)

## Modelo lineas de partidos
* Equipo
* Puntuación (que serán goles/canastas/etc)


# Vistas nuevos modelos
* Vistas embebidas para las líneas de liga y de partidos


# Vistas cont.
* Vista pivot, graph y calendario de los partidos

# Campos calculados
En los partidos, se debe calcular el equipo ganador dependiendo de la puntuación de las lineas.
En la liga, tiene que haber un botón rellene las líneas y calcule las puntuaciones de todos los equipos
