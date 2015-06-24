from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from catalogo.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        titulo = 'Catálogo de cursos'.encode('utf-8')
        self.assertIn(titulo, response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
