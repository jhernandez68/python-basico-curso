"""Ejemplo práctico de herencia de clases en Python.

Muestra:
- Clase base `Animal`
- Clases derivadas `Perro`, `Gato`
- Múltiple herencia con un *mixin* (`Volador`)
- Uso de `super()`
- Polimorfismo (misma interfaz en diferentes subclases)
"""

class Animal:
    """Clase base (padre). Contiene atributos y métodos comunes."""

    def __init__(self, nombre: str):
        self.nombre = nombre

    def hablar(self) -> str:
        """Método que se espera sobrescribir en cada subclase."""
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def __str__(self) -> str:
        return f"Soy un {self.__class__.__name__} llamado {self.nombre}"


class Perro(Animal):
    """Subclase que hereda de `Animal`."""

    def __init__(self, nombre: str, raza: str):
        super().__init__(nombre)          # llama al constructor de la clase base
        self.raza = raza

    def hablar(self) -> str:
        return "Guau! Guau!"


class Gato(Animal):
    """Otra subclase que hereda de `Animal`."""

    def hablar(self) -> str:
        return "Miau!"


class Volador:
    """Mixin que aporta la capacidad de volar."""

    def volar(self) -> str:
        return f"{self.nombre} está volando 🦇"


class Murcielago(Volador, Animal):
    """Ejemplo de **múltiple herencia**.

    El orden de las clases determina el *Method Resolution Order* (MRO).
    """

    def hablar(self) -> str:
        return "Chillido ultrasónico"


def main() -> None:
    animales: list[Animal] = [
        Perro("Firulais", "Labrador"),
        Gato("Misu"),
        Murcielago("Bruce")
    ]

    # Polimorfismo: cada objeto responde a `hablar` a su manera.
    for animal in animales:
        print(animal)              # __str__
        print(animal.hablar())     # método sobrescrito
        if isinstance(animal, Volador):
            # Solo Murcielago tiene el mixin Volador
            print(animal.volar())
        print("-" * 20)


if __name__ == "__main__":
    main()
