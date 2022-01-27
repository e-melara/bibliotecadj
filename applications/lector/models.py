from django.db import models

from .manager import PrestamoManager
from applications.libro.models import Libro
from applications.autor.models import Persona


class Lector(Persona):
    def __str__(self):
        return str(self.id) + " - " + self.nombre + " " + self.apellidos


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name="libro_prestamo"
    )
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    objects = PrestamoManager()

    def __str__(self):
        return str(self.id) + " " + self.libro.titulo
