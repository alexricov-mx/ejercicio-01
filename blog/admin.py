from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "categoria", "publicado", "creado_en")
    search_fields = ("titulo", "contenido", "categoria")
    list_filter = ("categoria", "publicado", "creado_en")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "autor", "post", "creado_en")
    search_fields = ("autor", "texto")
