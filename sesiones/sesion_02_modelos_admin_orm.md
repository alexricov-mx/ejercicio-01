# Sesion 2 - Modelos, admin y ORM

Duracion: **2 horas**

## Objetivos

- Crear modelos para persistir datos.
- Entender migraciones.
- Registrar modelos en admin.
- Hacer consultas basicas con ORM.

## Agenda (120 min)

- **0-20 min:** Repaso rapido de sesion 1.
- **20-55 min:** Modelado de datos (`Post`, `Comment`).
- **55-80 min:** Migraciones y base de datos.
- **80-105 min:** Django admin + superusuario.
- **105-120 min:** Consultas ORM en shell.

## Codigo base

## `blog/models.py`

```python
from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    publicado = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.CharField(max_length=120)
    texto = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor}"
```

## Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

## `blog/admin.py`

```python
from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "publicado", "creado_en")
    search_fields = ("titulo", "contenido")
    list_filter = ("publicado", "creado_en")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "autor", "post", "creado_en")
    search_fields = ("autor", "texto")
```

## Crear superusuario

```bash
python manage.py createsuperuser
```

Entrar a: `http://127.0.0.1:8000/admin`

## ORM basico (en shell)

```bash
python manage.py shell
```

```python
from blog.models import Post, Comment

post = Post.objects.create(titulo="Mi primer post", contenido="Contenido del post")
Comment.objects.create(post=post, autor="Ana", texto="Excelente contenido")

Post.objects.filter(publicado=True)
Post.objects.get(id=1)
post.comentarios.all()
```

## Mini ejercicio

- Agregar campo `categoria` al modelo `Post`.
- Aplicar migraciones.
- Mostrar `categoria` en admin.

## Tarea

- Crear 5 posts desde admin.
- Hacer 3 consultas ORM y guardar capturas/resultados.

## Evaluacion rapida

- Entiende el ciclo: modelo -> migracion -> DB.
- Sabe crear y consultar objetos con ORM.
