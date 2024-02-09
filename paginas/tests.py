from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class PruebasPaginaInicio(SimpleTestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertEqual(respuesta.status_code, 200)

    def test_nombre_plantilla_correcta(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertTemplateUsed(respuesta, 'inicio.html')

    def test_contenido_plantilla(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertContains(respuesta, '<h1>P&aacute;gina de Inicio</h1>')

class PruebasPaginaNosotros(SimpleTestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get('/nosotros/')
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse('nosotros'))
        self.assertEqual(respuesta.status_code, 200)

    def test_nombre_plantilla_correcta(self):
        respuesta = self.client.get(reverse('nosotros'))
        self.assertTemplateUsed(respuesta, 'nosotros.html')

    def test_contenido_plantilla(self):
        respuesta = self.client.get(reverse('nosotros'))
        self.assertContains(respuesta, '<h1>Nosotros</h1>')
