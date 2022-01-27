from django.db import models


class Persona(models.Model):
    edad = models.IntegerField()
    pais = models.CharField("Pais", max_length=50)
    full_name = models.CharField('nombres', max_length=50)
    pasaporte = models.CharField("Pasaporte", max_length=50)
    apelativo = models.CharField("Apelativo", max_length=50)

    class Meta:
        db_table = 'persona'
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        unique_together = ['pais', 'apelativo']
        constraints = [
            models.CheckConstraint(
                check=models.Q(edad__gte=18), name='mayor_edad_18'
            )
        ]

    def __str__(self):
        return self.full_name


class Empleado(Persona):
    empleo = models.CharField("Empleo", max_length=50)
