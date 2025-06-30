"""Ejemplos de uso del *if* con operadores lógicos.

Ejecuta el script y proporciona la información solicitada
para ver cómo se comportan las distintas condiciones.
"""

# Pedimos la edad del usuario y la convertimos a entero
age = int(input("Introduce tu edad: "))

# ------------------------------------------------------------------------
# Esto es un caso con AND
# ------------------------------------------------------------------------
# Solo será mayor de edad si se cumplen *ambas* condiciones:
#   1) age >= 18
#   2) age <= 120  → evitamos valores absurdamente altos
if age >= 18 and age <= 120:
    print("Mayor de edad (condición con AND)")

# ------------------------------------------------------------------------
# Esto es un caso con NOT
# ------------------------------------------------------------------------
# `not` invierte el valor booleano.
# Cualquier entero distinto de 0 es *truthy*, mientras que 0 es *falsy*.
if not age:
    print("Has introducido 0, que se evalúa como False")

# ------------------------------------------------------------------------
# Esto es un caso con OR
# ------------------------------------------------------------------------
# El operador OR devuelve el primer operando *truthy*.
# Sirve para asignar valores por defecto.
valor_defecto = age or 18
print("Resultado de 'age or 18':", valor_defecto)
