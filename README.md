# IMPORTACIONES COLOMBIA 2023

Proyecto que provee apis para el análisis de los procesos de importación realizados en el 2023 en Colombia .

## Herramientas

* Python
* Django Framework
* Postgres

## Clonando del proyecto

Primero debe clonar este repositorio usando el comando:

```
$ git clone https://github.com/florez18399/imports_colombia_back.git
```

## Configuración base de datos
Para este proyecto se creó una db llamada `db_imp_colom` en postgtres, adicionalmente se 
ejecutaron los scripts presentes en los archivo inserts_paises.sql para la creación
de una tabla países.


## Instalando el proyecto

Activar entorno virtual
```
pip install virtualenv

virtualenv env

.\env\Scripts\activate
```

Instalar librerías
```
$ pip install -r requirements.txt
```
Ejecutar migraciones
```
$ python manage.py makemigrations
$ python manage.py migrate
```

Ejecutando el script de inserción de datos 

```
$ python load_data.py
```

Finalmente, para ejecutar el servidor de **Django** se debe usar el siguiente comando en una consola:

```
$ python manage.py runserver
```

## Funcionamiento del proyecto

- Para ingresar a la API en el navegador ingrese el siguiente link <http://127.0.0.1:8000/api/>

Si desea revisar los datos subidos al proyecto lo puede realizar desde el `admin`:

- Cree un usuario administrador con el comando:

```
$ python manage.py createsuperuser
```

Una vez creado el usuario, para ingresar al `admin` en el navegador ingrese el siguiente link <http://127.0.0.1:8000/admin>

## Endpoints de la API

1. Para hacer una petición GET a todos los datos del proyecto:

```
GET http://localhost:8000/imports/
```