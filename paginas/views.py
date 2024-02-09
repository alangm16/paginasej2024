#from django import template
from django.views.generic import TemplateView

# Create your views here.
class VistaPaginaInicio(TemplateView):
    template_name = 'inicio.html'

class VistaNosotros(TemplateView):
    template_name = 'nosotros.html'    