from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path('prestamo/add',
         view=views.RegistrarPrestamo.as_view(),
         name='add-prestamo'
         ),
    path('prestamo-multiple',
         view=views.AddMultiplePrestamo.as_view(),
         name='multiple-prestamo'
         )
]
