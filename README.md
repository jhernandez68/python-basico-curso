# Python Básico – Curso

Repositorio con apuntes y ejemplos para un curso introductorio de **Python**.

## Estructura

| Carpeta | Descripción |
|---------|-------------|
| `1.que_es_python/` | Introducción: qué es Python y cómo instalarlo con **pyenv**. |
| `2.conceptos_basicos/` | Conceptos básicos del lenguaje (operadores lógicos, funciones *built‑in*, etc.). |

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

Jhoan Hernández – [@jhhernandez68](https://github.com/jhernandez68)

