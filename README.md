# Python Básico – Curso

Repositorio con apuntes y ejemplos para un curso introductorio de **Python**.

## Estructura

| Carpeta | Descripción |
|---------|-------------|
| `1.que_es_python/` | Introducción: qué es Python y cómo instalarlo con **pyenv**. |
| `2.conceptos_basicos/` | Conceptos básicos del lenguaje (operadores lógicos, funciones *built‑in*, etc.). |
| `3.estructuras_de_datos/` | Estructuras de datos fundamentales: listas, tuplas, diccionarios y sets, con ejemplos y scripts. |
| `4.condicionales/` | Uso de estructuras condicionales (`if`, `else`, `elif`), operadores lógicos (`and`, `or`, `not`) y buenas prácticas. |
| `5.ciclos/` | Bucles de repetición (`for`, `while`), cláusulas `else`, control de flujo (`break`, `continue`) |


## Instalación rápida

```bash
# Clona el repositorio
git clone https://github.com/jhernandez68/python-basico-curso
cd Python2025

# Instala Python con pyenv (ejemplo con 3.12.3)
pyenv install 3.12.3
pyenv local 3.12.3
```

> Asegúrate de tener las dependencias de compilación instaladas.  
> Consulta `1.que_es_python/instalacion_pyenv.md` para más detalles.

## Cómo usar el material

1. Navega a cada carpeta para leer los archivos `.md` y ejecutar los ejemplos `.py`.
2. Activa el entorno local de `pyenv` en la raíz del proyecto:  
   ```bash
   pyenv activate .
   ```
3. Ejecuta los scripts con:

```bash
python ejemplo.py
```


## Autor

Jhoan Hernández – [@jhernandez68](https://github.com/jhernandez68)

