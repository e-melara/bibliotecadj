from django.db import models
from django.db.models import Q


class AutorManager(models.Manager):
    def buscar_autor(self, kword):
        resultado = self.filter(
            nombre__icontains=kword
        )
        return resultado

    def buscar(self, kword):
        resultado = self.filter(
            Q(nombre__icontains=kword) |
            Q(apellidos__icontains=kword)
        )

        return resultado

    def buscarExcludeYear(self, kword):
        return self.filter(
            Q(nombre__icontains=kword) | 
            Q(apellidos__icontains=kword)
        ).exclude(
            Q(edad__icontains=20)
        )
        
    def resultadoYearGt(self, kword):
        return self.filter(
            edad__gt=40,
            edad__lt=65
        ).order_by('apellidos', 'nombre')
        