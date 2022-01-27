from unicodedata import name
from django import views
from django.urls import path
from .views import LibroDetailView, LibroListView, ListLibro2, LibroTrgListView

urlpatterns = [
    path('libro-2/', view=ListLibro2.as_view(), name='lista-libro-2'),
    path('libros/', view=LibroListView.as_view(), name='listar_libros'),
    path('libros-trg/', view=LibroTrgListView.as_view(), name='libro_trg'),
    path('libro-detalle/<pk>/', view=LibroDetailView.as_view(), name='libro-details')
]
