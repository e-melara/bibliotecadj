from django.db import models


class Author(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre + "-" + self.apellidos
