"""Ejemplo de *else* y operador OR.

Muestra cómo otorgar distintos tipos de acceso
según el nombre introducido.
"""

name = input("Introduce tu nombre de usuario: ")

# Comprobamos si el usuario es administrador.
# - is_admin es True si name == 'admin'
# - name.startswith('root') detecta usuarios que comienzan por 'root'
# ------------------------------------------------------------------------
# Esto es un caso con OR
# ------------------------------------------------------------------------
if name.lower() == "admin" or name.startswith("root"):
    # La rama *if* se ejecuta si al menos UNA de las condiciones es verdadera.
    print("Acceso total")
else:
    # La rama *else* cubre todos los demás casos.
    print("Acceso limitado")
