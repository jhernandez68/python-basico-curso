#!/usr/bin/env python3
"""Uso de *elif* (else‑if) para clasificar una nota.

Cuando existe una secuencia de condiciones **mutuamente exclusivas**
y queremos ejecutar SOLO la primera que se cumpla, usamos *elif*.
Evita encadenar varios *if* independientes y hace el código más claro.
"""

score = float(input("Introduce tu nota (0‑100): "))

# Cada `elif` se evalúa solo si las condiciones anteriores fueron falsas.
if score >= 90:
    print("Sobresaliente (>= 90)")
elif score >= 80:
    print("Excelente (80‑89)")
elif score >= 70:
    print("Bueno (70‑79)")
else:
    # Rama por defecto cuando ninguna condición previa se cumple.
    print("Insuficiente (< 70)")

# ------------------------------------------------------------------------
# Curiosidad: combinación de AND y NOT dentro de un ELIF
# ------------------------------------------------------------------------
# Demostración de evaluación de rangos con lógica booleana.
if score and isinstance(score, float):
    print("La variable 'score' es un número válido (truthy) de tipo float")
