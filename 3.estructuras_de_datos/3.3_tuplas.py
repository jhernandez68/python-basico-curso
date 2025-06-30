'''
Son similares a las listas pero son INMUTABLES, es decir, no pueden cambiar sus valores.
Se pueden declarar sin utilizar los parentesis
Tienen menor tiempo de procesamiento
'''

lenguajes = ("python", "c", "c++")
lenguajes_sin_parentesis = "python", "c", "c++"

#Para acceder a un elemento se utiliza su posición

print(lenguajes[0])

lenguajes[0] = "java" #da error apropósito.