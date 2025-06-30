"""Ejemplos de bucle *while* en Python.

Incluye:
- Cuenta atrás con `while`
- Palabras clave `break`, `continue`, `else`
- Emulación de un bucle *do‑while*
"""

# --------------------------
# Cuenta atrás sencilla
# --------------------------
contador = 3
while contador > 0:
    print("Cuenta atrás:", contador)
    contador -= 1
else:  # se ejecuta cuando el while finaliza SIN break
    print("¡Despegue!")

# --------------------------
# Búsqueda con break
# --------------------------
objetivos = [2, 4, 6, 8]
idx = 0
buscar = 6

while idx < len(objetivos):
    if objetivos[idx] == buscar:
        print("Encontrado en índice", idx)
        break
    idx += 1
else:
    print("No encontrado")

# --------------------------
# Emular un do‑while
# Python no tiene bucle `do‑while` nativo.
# Se usa un `while True:` y se rompe con `break`.
# --------------------------
while True:
    cmd = input("Escribe 'salir' para terminar: ").lower()
    if cmd == "salir":
        print("Adiós")
        break
    print("Comando inválido, intenta de nuevo")
