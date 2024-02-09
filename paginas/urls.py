#paginas/urls.py
from django.urls import path
from .views import VistaPaginaInicio , VistaNosotros

urlpatterns = [
    path('', VistaPaginaInicio.as_view(),name='inicio'),
    path('nosotros/',VistaNosotros.as_view(),name='nosotros'),
]