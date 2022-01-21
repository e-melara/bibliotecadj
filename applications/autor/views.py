from django.views.generic import ListView
from .models import Author


class AutorListView(ListView):
    context_object_name = "lista_autores"
    template_name = "autores/lista.html"
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        
        # return Author.objects.buscar_autor(palabra_clave)
        # return Author.objects.buscarExcludeYear(palabra_clave) 
        return Author.objects.resultadoYearGt(palabra_clave)