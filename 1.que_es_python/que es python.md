# ¿Qué es Python?

Python es un lenguaje de programación de alto nivel, interpretado y multiparadigma, conocido por su sintaxis clara y legible. Fue creado en 1991 por Guido van Rossum y se utiliza en desarrollo web, ciencia de datos, automatización, inteligencia artificial, scripting y muchas otras áreas gracias a su extenso ecosistema de bibliotecas.

## Ventajas principales

- **Sintaxis sencilla** que facilita el aprendizaje y la mantenibilidad del código.
- **Gran comunidad** y abundante documentación.
- **Portabilidad** entre sistemas operativos.
- **Extensa colección de módulos y paquetes** disponibles en PyPI.
- **Apoyo a múltiples paradigmas**: orientado a objetos, funcional, imperativo.

# Instalación de Python con pyenv

`pyenv` es una herramienta que permite instalar y gestionar múltiples versiones de Python en el mismo sistema sin interferir con las del sistema operativo.

## Pasos

1. Instalar dependencias de compilación.
2. Instalar `pyenv`.
3. Configurar el entorno de shell.
4. Instalar la versión de Python deseada.
5. Establecer la versión global o crear entornos específicos.

### 1. Instalar dependencias (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install -y build-essential curl git make libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

### 2. Instalar pyenv

```bash
curl https://pyenv.run | bash
```

### 3. Configurar el shell

Añade al final de `~/.bashrc`, `~/.zshrc` u otro archivo de inicio las siguientes líneas y vuelve a cargar la sesión:

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

### 4. Instalar una versión de Python

```bash
pyenv install 3.12.3
```

### 5. Elegir la versión global

```bash
pyenv global 3.12.3
```

Con esto tendrás Python 3.12.3 instalado y activo por defecto. Puedes verificarlo con:

```bash
python --version
```

Para listar versiones disponibles o instaladas:

```bash
pyenv install --list
pyenv versions
```

Para crear un entorno virtual aislado basado en la versión actual:

```bash
pyenv virtualenv 3.12.3 venv-proyecto
```

Luego, dentro del directorio del proyecto:

```bash
pyenv local venv-proyecto
```

De esta forma, cualquier terminal abierta en ese directorio usará automáticamente el entorno virtual `venv-proyecto`.
