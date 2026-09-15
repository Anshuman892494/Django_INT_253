from django.http import response
from django.test import TestCase

# Create your tests here.

class HomeViewTest(TestCase):
    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_resolves(self):
        response = self.client.get('/dash/')
        self.assertEqual(response.status_code, 200)
    
    def test_template_name(self):
        response = self.client.get('/dash/')
        self.assertTemplateUsed(response, 'dash.html')

    def test_contains_code(self):
        response = self.client.get('/')
        self.assertContains(response, "Welcome to My Homepage!")
       
    # 1. Run tests
    # python manage.py test

    # python manage.py test homepage.tests.HomeViewTest
