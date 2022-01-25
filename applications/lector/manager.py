from django.db import models

from django.db.models import Avg, Sum, Count


class PrestamoManager(models.Manager):
    def libros_promedio_edades(self):
        return self.filter(
            libro__id="3"
        ).aggregate(
            promedio_edad=Avg("lector__edad"),
            suma_edad=Sum("lector_edad")
        )

    def num_libros_prestamos(self):
        resultado = self.values(
            'libro'
        ).annotate(
            num_prestados=Count('libro')
        )

        for r in resultado:
            print(r)

        return resultado
