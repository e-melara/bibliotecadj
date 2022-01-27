from datetime import date
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .models import Prestamo
from .forms import PrestamoForm, MulitplePrestamoForm


class RegistrarPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = reverse_lazy('add-prestamo')

    def form_valid(self, form):
        # Prestamo.objects.create(
        #     lector=form.cleaned_data['lector'],
        #     libro=form.cleaned_data['libro'],
        #     fecha_prestamo=date.today(),
        #     devuelto=False
        # )
        # prestamo = Prestamo(
        #     lector=form.cleaned_data['lector'],
        #     libro=form.cleaned_data['libro'],
        #     fecha_prestamo=date.today(),
        #     devuelto=False
        # )
        # prestamo.save()
        obj, created = Prestamo.objects.get_or_create(
            devuelto=False,
            libro=form.cleaned_data['libro'],
            lector=form.cleaned_data['lector'],
            defaults={
                'fecha_prestamo': date.today()
            }
        )
        if created:
            return super(RegistrarPrestamo, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')


class AddMultiplePrestamo(FormView):
    form_class = MulitplePrestamoForm
    template_name = 'lector/add_multiple_prestamo.html'
    success_url = reverse_lazy('multiple-prestamo')

    def form_valid(self, form):
        print(form.cleaned_data['lector'])
        print(form.cleaned_data['libros'])

        prestamos = []
        for l in form.cleaned_data['libros']:
            prestamo = Prestamo(
                libro=l,
                devuelto=False,
                fecha_prestamo=date.today(),
                lector=form.cleaned_data['lector'],
            )
            prestamos.append(prestamo)
        Prestamo.objects.bulk_create(
            prestamos
        )
        return super(AddMultiplePrestamo, self).form_valid(form)
