# Traductor AFI

Este es un proyecto de Flask que se puede empaquetar en un archivo ejecutable de Windows.

## Requisitos

Para ejecutar este proyecto, necesitarás:

- Python 3.9: Puedes descargarlo desde [la página oficial de Python](https://www.python.org/downloads/).
- Git: Puedes descargarlo desde [la página oficial de Git](https://git-scm.com/downloads).

## Clonar el Proyecto

Para clonar este proyecto, ejecuta el siguiente comando en tu terminal:

```bash
git clone https://github.com/notami18/translator-afi.git
```

## Crear un Ejecutable de Windows

Instalar pyinstaller:

```bash
pip install pyinstaller
```

Ejecutar PyInstaller para empaquetar la aplicación:

```bash
pyinstaller --onefile --windowed start.py
```

Después de ejecutar este comando, encontrarás el archivo ejecutable en la carpeta dist en la raíz del proyecto.
