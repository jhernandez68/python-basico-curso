'''
Se pueden tener variables como parametros () e instanciarlos al llamar la función.
Las variables locales se definen en el bloque de la función, no se pueden utilizar por fuera de la función.
Las variables globales pueden ser utilizadas por fuera de la función, ya que son definidas fuera de este.
'''

VARIABLE_GLOBAL = "Hola, soy una variable global!" #se suele definir en mayuscula

def saludar_variable_local():
    nombre_completo = "Jhoan Hernandez" #nombre completo solo se puede utilizar en este bloque
    print(nombre_completo)


def saludar_persona(nombre):
    VARIABLE_GLOBAL = "Hola, mi valor cambió a este" #Este valor solo funciona en el bloque de la función, una vez terminado vuelve a ser igual
    print(VARIABLE_GLOBAL)
    print("Hola "+ nombre)


saludar_variable_local()
saludar_persona("Jhoan")
print(VARIABLE_GLOBAL) #Imprime el valor original


'''
Para varios parametros se puede llamar de dos maneras:
'''

def perimetro_cuadrado(lado, unidad_medida):
    perimetro = lado * 4
    print(f"El perimetro es de {perimetro} {unidad_medida}")

perimetro_cuadrado(25, "Metros")
perimetro_cuadrado(unidad_medida="Metros", lado=25)