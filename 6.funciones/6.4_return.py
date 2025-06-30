'''
Para retornar un valor mediante una funcion se utiliza la palabra reservada return.
El valor retornado se puede almacenar en otra variable
'''

def perimetro_cuadrado(lado):
    perimetro = lado * 4
    return perimetro

def area_cuadrado(lado):
    area = lado * lado
    return area

perimetro = perimetro_cuadrado(10)
area = area_cuadrado(10)

print(perimetro)
print(area)

