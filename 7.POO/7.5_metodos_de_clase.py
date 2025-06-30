'''
Se definen como las funciones, pero reciben como atributo la propiedad self
'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumplir_anios(self): #es un método de la clase
        self.edad = self.edad + 1
        print(f"Feliz cumpleaños #{self.edad} {self.nombre}")

Jhoan = Persona(nombre="Jhoan", edad=24)

Jhoan.cumplir_anios() #self no cuenta como parametro