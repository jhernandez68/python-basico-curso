#Se definen entre [] y sus elementos son separados por ,

lenguajes = ["python", "java", "c++"]

print(lenguajes) #Se imprimen en el orden python, java, c++

lista = [1, 2.0, True, "python", 1] #mantiene los elementos repetidos.

print (lista)

'''
Manejando las listas sutilmente
'''

print(lenguajes[0]) #Imprime python
print(lenguajes[-1]) #Imprime c++, ya que es el ultimo elemento de la lista
print(len(lenguajes)) #Imprime 3
print(lenguajes[0:2]) #Imprime python y java

#una lista de listas
programacion = [lenguajes, "dedicación", "practica"]
print(programacion)

#accediendo a la programacion -> lenguajes
print(programacion[0][0])


'''
Son mutables
Es decir, que se pueden cambiar sus valores
'''
lenguajes[1] = "Javascript"
print(lenguajes)


'''
Para añadir elementos a la lista se utiliza la funcion append
'''

lenguajes.append("python")

print(lenguajes)


'''
Para 'sumar' dos listas se utiliza la función extend
'''

otros_lenguajes = ["c"]
lenguajes.extend(otros_lenguajes)

print (lenguajes)