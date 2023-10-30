# Proyecto 1, parte 2
Repositorio para la segunda parte del proyecto del curso.

Integrantes:
- Federico Melo Barrero, 202021525, f.melo. Sección 1.
- Shadith Pérez Rivera, 202014687, s.perezr. Sección 2.

## Instalación

### Requisitos

- Python 3.8 o superior
- pip (Gestor de paquetes de Python)
- virtualenv (Gestor de entornos virtuales de Python)

## Pasos para ejecutar la aplicación

1. Clonar el repositorio
   Puedes clonar el repositorio usando el siguiente comando:
   ```
   git clone https://github.com/fedemelo/profile-manager-back
   ```
   
2. Crear un entorno virtual con las dependencias

Instalar virtualenv usando pip:

```
pip install virtualenv
```

Crear un entorno virtual:

```
python -m virtualenv env
```

Activar el entorno virtual:

```
env\Scripts\activate.bat
```

Instalar las dependencias:

```
pip install -r requirements.txt
```

3. Ejecutar la aplicación

Ejecutar la aplicación con el siguiente comando:

```
python -m uvicorn src.main:app --reload
```

La aplicación estará en ejecución en http://127.0.0.1:8000/.

Puedes acceder a la aplicación a través de un navegador o utilizando una herramienta como Postman.

### Documentación de la API
La documentación de la API está disponible en http://127.0.0.1:8000/, creada automáticamente por Swagger UI.
