# Proyecto 1, parte 2
Repositorio para la segunda parte del proyecto del curso.

Integrantes:
- Federico Melo Barrero, 202021525, f.melo. Sección 1.
- Shadith Pérez Rivera, 202014687, s.perezr. Sección 2.

## Instalación del Backend

### Requisitos

- Python 3.8 o superior
- pip (Gestor de paquetes de Python)
- virtualenv (Gestor de entornos virtuales de Python)

### Pasos para ejecutar la aplicación

1. Clonar el repositorio
   
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


## Instalación del Frontend

### Requisitos

- Node.js
- Yarn

### Pasos para ejecutar la aplicación

1. Clonar el repositorio

2. Instalar node. Puedes verificar que node se ha instalado usando el siguiente comando:
```
node -v
```

Instala yarn, usando el siguiente comando:
```
npm install --global yarn
```

Puedes verificar que yarn se ha instalado usando el siguiente comando:
```
yarn -v
```

Añade los scripts al archivo package.json:
```
yarn add react-scripts
```
Instala las dependencias:
```
yarn install
```

3. Ejecutar la aplicación
Ejecuta la aplicación usando el siguiente comando:
```
yarn start
```

La aplicación estará en funcionamiento en http://172.23.160.1:3000

Puedes acceder a la aplicación a través de un navegador.

### Notas importantes
Para que la aplicación funcione correctamente, debes ejecutar la aplicación del backend, con las instrucciones anteriores.

Para autenticarte correctamente, debes usar un usuario que ya esté registrado en la base de datos. Puedes encontrar los usuarios registrados en la aplicación del backend, usando el siguiente endpoint:
http://127.0.0.1:8000/logins/

Alternativamente, puedes usar uno de los siguientes usuarios, que ya están registrados en la base de datos:

Nombre de usuario: "admin",
Contraseña: "password"
