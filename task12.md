# Crear modelo de entradas
* Nombre
* Cliente
* Partido

# Herencia por extensión
* En el modulo nuevo heredar el modelo de entradas y añadir un many2one de pedido de venta
* Heredar sale.order y añadirle un botón para que cree una entrada para un partido
* Heredar el botón de cancelar de pedido de venta y eliminar las entradas cuando se cancele el pedido

# Herencia por delegación
* En el modelo de jugadores que tenemos añadirle herencia por delegación con inherits y probar después a añadir a la vista campos de res.partner como por ejemplo street,city y country_id
