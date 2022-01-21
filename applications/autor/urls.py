from django.urls import path
from .views import AutorListView


urlpatterns = [
    path("autores/", view=AutorListView.as_view(), name='autores')
]
