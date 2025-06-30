'''
Sirven para guardar elementos unicos, son guardados entre {} y separados por comas
No se pueden obtener indices, ya que tienen elementos únicos
setError = {1,1,1,2} -> guardaria solo 1,2
'''
set1 = {1,2,3}

#Para añadir un elemento se utiliza la función add()
set2 = set1
set2.add(3) #no se añade, ya que estaba antes en set1
set2.add(4)
print(set2)

#para borrar un elemento se usa .discard()
set2.discard(2)
print(set2)

#para eliminar un elemento se utiliza .remove(), pero si se intenta eliminar uno que no existe da error
set2.discard(3)
print(set2)

#para vaciar TODO el set se utiliza la funcion .clear()
set2.clear()
print(set2) #retorna un set vacio

