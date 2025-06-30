'''
Utilizan llave y valor, se definen entre llaves {}, cada elemento es separado mediante comas

NO se pueden tener dos llaves iguales al diccionario, esto da error.

Puede contener listas
'''

lenguaje = {
    "nombre": "python",
    "creador": "Guido"
}

print(lenguaje)

#No se utilizan indices para acceder a los elementos, se utilizan las llaves, por ejemplo 'nombre'
print(lenguaje["nombre"])

#Para añadir un elemento al diccionario
lenguaje["anio_lanzamiento"] = 1991
print(lenguaje)

lenguaje["caracteristicas"] = ["Sencillo", "Facil"]
print(lenguaje)

#para imprimir la lista de las llaves del diccionario se utiliza .keys()
print(lenguaje.keys())