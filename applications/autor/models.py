from django.db import models
from .manager import AutorManager


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Author(Persona):
    seudonimo = models.CharField("seudonimo", max_length=50, blank=True)
    objects = AutorManager()

    def __str__(self):
        return str(self.id) + " - " + self.nombre + "-" + self.apellidos
