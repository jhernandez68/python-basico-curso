"""Demostración de manejo de excepciones con try/except/else/finally."""

def leer_entero():
    """Solicita un número al usuario y lo devuelve como int."""
    while True:
        try:
            return int(input("Introduce un número entero: "))
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")

def dividir(a: int, b: int) -> float:
    """Divide *a* entre *b* y maneja división por cero."""
    try:
        resultado = a / b
    except ZeroDivisionError as exc:
        print("Error:", exc)
        resultado = float('inf')  # valor por defecto
    else:
        print("División exitosa")
    finally:
        print("Fin de la operación dividir()\n")
    return resultado

def main() -> None:
    x = leer_entero()
    y = leer_entero()
    print(f"{x} / {y} =", dividir(x, y))

if __name__ == "__main__":
    main()
