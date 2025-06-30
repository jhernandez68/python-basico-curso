"""Ejemplos de bucle *for* en Python.

Incluye:
- Recorrido de listas
- Uso de `range` y `enumerate`
- Palabras clave `continue`, `break`, `else`
"""

frutas = ["manzana", "pera", "uva", "mango"]

# --------------------------
# Recorrer una lista
# --------------------------
for fruta in frutas:
    print(fruta)

# --------------------------
# range(inicio, fin, paso)
# --------------------------
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print("Número:", i)

# --------------------------
# enumerate(iterable, start)
# Devuelve tuplas (índice, valor)
# --------------------------
for idx, fruta in enumerate(frutas, 1):
    print(f"{idx}. {fruta}")

# --------------------------
# continue salta a la siguiente iteración
# break sale del bucle
# --------------------------
for n in range(10):
    if n % 2 == 0:
        continue  # salta los pares
    if n > 7:
        break     # detiene el bucle
    print("Impar menor que 8:", n)

# --------------------------
# Cláusula else en for
# Se ejecuta si NO se encuentra un break
# --------------------------
objetivos = [3, 8, 15]
buscar = 4
for valor in objetivos:
    if valor == buscar:
        print("Encontrado", buscar)
        break
else:
    print(buscar, "no está en la lista")
