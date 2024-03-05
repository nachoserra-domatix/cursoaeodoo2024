# Añadir seguridad (7)

Hacer dos grupos de usuario, manager y user.
El usuario solo podrá ver y modificar los tickets que tenga asignados (crearemos un campo user_id)
El manager podrá crear, borrar ver y modificar cualquier ticket

# Mejorar vista (9)
Añadir campos secuencia(integer), soluciones(html) y responsable(many2one)

## Vista tipo lista:
Añadir campo sequence con widget handle
Mostrar nombre, asignado, fecha y estado
Campo fecha que sea opcional y mostrarlo por defecto
Campo asignado que sea opcional pero ocultarlo

## Vista formulario
Header con el estado, nombre h1 como en pedidos y dos columnas:
Fecha
Asignado / Asistencia

## Solapas:
Descripcion y soluciones
