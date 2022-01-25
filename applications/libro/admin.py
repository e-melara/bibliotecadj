from django.contrib import admin
from .models import Libro, Categoria

admin.site.register(Categoria)
admin.site.register(Libro)
