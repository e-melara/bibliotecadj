from django.views.generic import ListView, DetailView
from .models import Libro


class LibroListView(ListView):
    context_object_name = 'lista_libro'
    template_name = "libros/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        fecha1 = self.request.GET.get('fecha1', '')
        fecha2 = self.request.GET.get('fecha2', '')

        if fecha1 and fecha2:
            return Libro.objects.listarOfDate(palabra_clave, fecha1, fecha2)
        else:
            return Libro.objects.listar_libro(palabra_clave)


class ListLibro2(ListView):
    context_object_name = 'lista_libro'
    template_name = "libros/lista2.html"

    def get_queryset(self):
        # return Libro.objects.listar_libro_categoria('4')
        return Libro.objects.listar_autor_categoria(3)


class LibroDetailView(DetailView):
    model = Libro
    template_name = "libros/details.html"
