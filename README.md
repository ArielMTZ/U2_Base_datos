# Proyecto de pruebas con Docker

Este proyecto ejecuta las pruebas automatizadas de la calculadora dentro de un contenedor Docker. La imagen instala las dependencias de `Calculadora/requirements.txt` y ejecuta `pytest`; no inicia un servidor web.

## Requisitos

- Docker Desktop instalado y en ejecución.
- Docker Compose v2 (`docker compose`), incluido en Docker Desktop.

## Ejecutar las pruebas con Docker Compose

Desde la carpeta raíz del proyecto, ejecuta el servicio de pruebas:

```powershell
docker compose run --build --rm tests
```

Docker construye la imagen si es necesario, instala `pytest` y ejecuta las pruebas. Un resultado exitoso muestra `3 passed`; si alguna prueba falla, el comando termina con un código distinto de cero.

También puedes construir la imagen y ejecutarla sin Compose:

```powershell
docker build -t calculadora-tests .
docker run --rm calculadora-tests
```

## Ejecutar las pruebas sin Docker

```powershell
cd Calculadora
python -m pip install -r requirements.txt
python -m pytest -q
```
