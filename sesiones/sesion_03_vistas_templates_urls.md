# Sesion 3 - Vistas, URLs y templates

Duracion: **2 horas**

## Objetivos

- Construir vistas basadas en funciones.
- Manejar parametros en URLs.
- Renderizar templates con contexto.
- Crear layout base reutilizable.

## Agenda (120 min)

- **0-15 min:** Repaso modelos/admin.
- **15-45 min:** Vistas de listado y detalle.
- **45-70 min:** Configuracion de templates.
- **70-95 min:** Herencia de templates (`base.html`).
- **95-120 min:** Ejercicio guiado + dudas.

## Vistas en `blog/views.py`

```python
from django.shortcuts import get_object_or_404, render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(publicado=True).order_by("-creado_en")
    return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, publicado=True)
    return render(request, "blog/post_detail.html", {"post": post})
```

## URLs en `blog/urls.py`

```python
from django.urls import path
from .views import post_detail, post_list

urlpatterns = [
    path("", post_list, name="post_list"),
    path("post/<int:post_id>/", post_detail, name="post_detail"),
]
```

## Template base `templates/base.html`

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}Blog Escolar{% endblock %}</title>
</head>
<body>
  <header>
    <h1>Blog Escolar</h1>
    <hr>
  </header>

  <main>
    {% block content %}{% endblock %}
  </main>
</body>
</html>
```

## Lista `templates/blog/post_list.html`

```html
{% extends "base.html" %}
{% block title %}Lista de posts{% endblock %}

{% block content %}
  <h2>Publicaciones</h2>
  {% for post in posts %}
    <article>
      <h3><a href="{% url 'post_detail' post.id %}">{{ post.titulo }}</a></h3>
      <p>{{ post.contenido|truncatechars:120 }}</p>
    </article>
  {% empty %}
    <p>No hay publicaciones aun.</p>
  {% endfor %}
{% endblock %}
```

## Detalle `templates/blog/post_detail.html`

```html
{% extends "base.html" %}
{% block title %}{{ post.titulo }}{% endblock %}

{% block content %}
  <article>
    <h2>{{ post.titulo }}</h2>
    <p>{{ post.contenido }}</p>
  </article>
  <a href="{% url 'post_list' %}">Volver</a>
{% endblock %}
```

## Mini ejercicio

- Mostrar cantidad de comentarios por post en la lista.
- Agregar fecha de publicacion formateada.

## Tarea

- Crear una pagina `contacto/` con su template.
- Personalizar `base.html` con menu simple.

## Evaluacion rapida

- Comprende flujo: URL -> vista -> template.
- Usa herencia de templates y filtros basicos.
