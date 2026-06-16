# Sesion 4 - Formularios y CRUD completo

Duracion: **2 horas**

## Objetivos

- Usar `ModelForm` para crear/editar datos.
- Implementar operaciones CRUD.
- Entender validaciones y mensajes de error.

## Agenda (120 min)

- **0-20 min:** Repaso de vistas/templates.
- **20-45 min:** Crear `PostForm`.
- **45-80 min:** Crear y editar posts.
- **80-105 min:** Eliminar posts.
- **105-120 min:** Practica guiada.

## `blog/forms.py`

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "publicado"]
```

## `blog/views.py` (CRUD)

```python
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from .models import Post

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})

def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form})

def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect("post_list")
    return render(request, "blog/post_confirm_delete.html", {"post": post})
```

## `blog/urls.py` (agregar rutas)

```python
path("post/nuevo/", post_create, name="post_create"),
path("post/<int:post_id>/editar/", post_update, name="post_update"),
path("post/<int:post_id>/eliminar/", post_delete, name="post_delete"),
```

## Template `templates/blog/post_form.html`

```html
{% extends "base.html" %}
{% block content %}
  <h2>Formulario de Post</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Guardar</button>
  </form>
{% endblock %}
```

## Template `templates/blog/post_confirm_delete.html`

```html
{% extends "base.html" %}
{% block content %}
  <h2>Eliminar post</h2>
  <p>¿Seguro que deseas eliminar "{{ post.titulo }}"?</p>
  <form method="post">
    {% csrf_token %}
    <button type="submit">Si, eliminar</button>
  </form>
{% endblock %}
```

## Mini ejercicio

- Agregar validacion: titulo minimo 10 caracteres.
- Mostrar enlace de editar/eliminar en `post_detail.html`.

## Tarea

- Crear CRUD para `Comment`.
- Mejorar estilos del formulario con clases CSS.

## Evaluacion rapida

- Implementa CRUD funcional sin errores de CSRF.
- Entiende validaciones con `form.is_valid()`.
