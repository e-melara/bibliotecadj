import random
from django.core.management import BaseCommand

import faker.providers
from faker import Faker

from applications.autor.models import Author
from applications.libro.models import Categoria, Libro
from applications.lector.models import Lector, Prestamo

CATEGORIES = [
    "Científicos",
    "Literatura y lingüísticos",
    "De viaje",
    "Biografías",
    "Libro de texto",
    "Libros de gran formato",
    "De referencia o consulta",
    "Monografías",
    "Recreativos",
    "Poéticos",
    "Juveniles",
    "Ficción"
]


class Command(BaseCommand):
    help = "LLenar los datos del autor"

    def handle(self, *args, **kwargs):
        fake = Faker(['de_DE'])

        # Autores
        # for _ in range(15):
        #     Author.objects.create(
        #         nombre=fake.name(),
        #         apellidos=fake.last_name(),
        #         nacionalidad=fake.city(),
        #         edad=random.randint(5, 90)
        #     )

        # for c in CATEGORIES:
        #     Categoria.objects.create(
        #         nombre=c
        #     )

        # Libros
        # for _ in range(100):
        #     c = random.randint(1, 12)
        #     v = random.randint(1, 200)
        #     a = random.randint(1, 12)

        #     libro = Libro(
        #         categoria_id=c,
        #         visitas=v,
        #         fecha=fake.date(),
        #         portada=fake.image_url(),
        #         titulo=fake.language_name() + " " + fake.language_name(),
        #     )

        #     autor = Author.objects.get(pk=a)
        #     libro.save()
        #     libro.autores.add(autor)

        # Lectores
        # for _ in range(25):
        #     Lector.objects.create(
        #         nombres=fake.name(),
        #         apellidos=fake.last_name(),
        #         nacionalidad=fake.city(),
        #         edad=random.randint(5, 90)
        #     )

        # Prestamos
        # for _ in range(300):
        #     lector = random.randint(1, 25)
        #     libro = random.randint(104, 203)

        #     Prestamo.objects.create(
        #         lector_id=lector,
        #         libro_id=libro,
        #         fecha_prestamo=fake.date(),
        #         devuelto=random.randint(0, 1)
        #     )
