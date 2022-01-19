from django.db import models
from applications.autor.models import Author


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)


class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Author)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField("Fecha de lazamiento")
    portada = models.ImageField(upload_to='portada')
    visitas = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo
