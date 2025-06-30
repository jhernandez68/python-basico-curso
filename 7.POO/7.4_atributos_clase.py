'''
Cada clase puede tener atributos, siendo las variables que definen las caracteristicas del objeto.
Atributos de instancia: Se definen en el init
Atributos de clase: Son variables que se definen fuera del constructor
'''

class Persona:
    atributo = 123
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

Jhoan = Persona("Jhoan", 20)

print(Jhoan.nombre)
print(Jhoan.edad)
print(Jhoan.atributo)