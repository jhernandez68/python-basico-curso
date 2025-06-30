"""Ejemplos breves de *docstrings* y cómo consultarlos.

Ejecuta este script para ver las cadenas de documentación
con `help()` y el atributo `__doc__`.
"""

def suma(a, b):
    """Suma dos números.

    Args:
        a (float): Primer sumando.
        b (float): Segundo sumando.

    Returns:
        float: Resultado de *a + b*.
    """
    return a + b


def saludar(nombre: str = "Mundo") -> None:
    """Imprime un saludo por pantalla.

    Parámetros
    ----------
    nombre : str, opcional
        Nombre del destinatario. Por defecto, "Mundo".
    """
    print(f"Hola, {nombre} 👋")


if __name__ == "__main__":
    # Mostrar documentación mediante help()
    help(suma)

    # Acceder directamente a la cadena de documentación
    print("\nDocstring de 'saludar':\n", saludar.__doc__)
