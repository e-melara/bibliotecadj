from django.db import models

from django.db.models.signals import post_save
from applications.autor.models import Author

from PIL import Image
from .manager import LibroManager, CategoriaManager


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    objects = CategoriaManager()

    def __str__(self) -> str:
        return str(self.id) + " - " + self.nombre


class Libro(models.Model):
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ['titulo', 'fecha']

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="categoria_libro"
    )
    autores = models.ManyToManyField(Author)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField("Fecha de lazamiento")
    portada = models.ImageField(upload_to='portada')
    visitas = models.PositiveIntegerField()
    stok = models.PositiveIntegerField(default=0)

    objects = LibroManager()

    def __str__(self):
        return "{}-{}".format(self.id, self.titulo)


def optimize_image(sender, instance, **kwargs):
    print('====== Optimizado la imagen =========')
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)


post_save.connect(optimize_image, sender=Libro)
