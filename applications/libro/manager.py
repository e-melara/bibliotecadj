import datetime
from django.db import models
from django.db.models import Count


class CategoriaManager(models.Manager):
    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()

    def listar_categoria_libro(self):
        resultado = self.annotate(
            num_libros=Count("categoria_libro")
        )
        for r in resultado:
            print("********")
            print(r, "- Count: ", r.num_libros)
            print("********")
        return resultado


class LibroManager(models.Manager):
    def listar_libro(self, kword):
        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=('2021-01-01', '2022-01-22')
        )
        return resultado

    def listarOfDate(self, kword, f1, f2):
        date1 = datetime.datetime.strptime(f1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(f2, "%Y-%m-%d").date()

        return self.filter(
            fecha__range=(date1, date2)
        )

    def listar_libro_categoria(self, categoria):
        return self.filter(
            categoria__id=categoria
        ).order_by('titulo')

    def listar_autor_categoria(self, author):
        return self.filter(
            autores=author
        ).distinct()

    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro

    def libros_num_prestamos(self):
        resultado = self.aggregate(
            num_libros=Count("libro_prestamo")
        )

        return resultado
