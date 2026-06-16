# Sesion 1 - Introduccion a Django y setup

Duracion: **2 horas**

## Objetivos

- Entender que es Django y cuando usarlo.
- Preparar ambiente de desarrollo.
- Crear y ejecutar un primer proyecto.
- Comprender estructura base de un proyecto Django.

## Agenda (120 min)

- **0-20 min:** Contexto web (cliente-servidor, HTTP, MVC/MTV en Django).
- **20-45 min:** Instalacion de Python virtual env + Django.
- **45-75 min:** Crear proyecto `config` y app `blog`.
- **75-100 min:** Explorar archivos clave (`settings.py`, `urls.py`, `manage.py`).
- **100-120 min:** Primer endpoint "Hola Django" + preguntas.

## Paso a paso guiado

### 1) Crear entorno

```bash
python -m venv .venv
source .venv/bin/activate
pip install django
python -m django --version
```

### 2) Crear proyecto y app

```bash
django-admin startproject config .
python manage.py startapp blog
```

### 3) Registrar la app en `config/settings.py`

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",
]
```

### 4) Crear vista simple en `blog/views.py`

```python
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola chicos, bienvenidos a Django")
```

### 5) Crear `blog/urls.py`

```python
from django.urls import path
from .views import saludo

urlpatterns = [
    path("", saludo, name="saludo"),
]
```

### 6) Incluir rutas de `blog` en `config/urls.py`

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]
```

### 7) Ejecutar servidor

```bash
python manage.py runserver
```

Abrir: `http://127.0.0.1:8000/`

## Mini ejercicio en clase (15 min)

Cambiar el mensaje de bienvenida para que incluya:

- Nombre del curso
- Nombre del equipo
- Fecha actual (puede ser fija en texto por ahora)

## Tarea

- Investigar diferencia entre `startproject` y `startapp`.
- Crear una segunda vista en `blog/views.py` para `/acerca/`.

## Evaluacion rapida

- Crea entorno virtual y activa correctamente.
- Levanta servidor sin errores.
- Entiende la ruta de solicitud: URL -> vista -> respuesta.

# Apuntes Alex

## Estructura de carpetas

```
proyecto-1/
  templates/
    admin/
      login.html
  static/
    css/
      admin-login.css
```

## Configuracion de PATHS en config/settings.py para incluir **templates**

```
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # <- aquí
        "APP_DIRS": True
        ...        
    },
]
```

## Configuracion de PATHs en config/settings.py para archivos **estaticos** para Estilos

```
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

