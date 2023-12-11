from django.test import TestCase
from django.urls import reverse

class LoginTests(TestCase):

    def test_login_form_valid_data(self):
        form_data = {'email': 'test@example.com', 'password': 'testpassword'}
        response = self.client.post(reverse('login'), data=form_data)
        self.assertEqual(response.status_code, 200)  

    def test_login_form_empty_data(self):
        form_data = {'email': '', 'password': ''}
        response = self.client.post(reverse('login'), data=form_data)
        self.assertEqual(response.status_code, 200)  

    def test_login_view(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, 'Hola! Ingresa tu e-mail y Contraseña')


class CreateUserFormTests(TestCase):

    def test_create_user_form_valid_data(self):
        form_data = {
            'user_type': 'adoptante',
            'name': 'John',
            'lastname': 'Doe',
            'phoneNumber': '123456789',
            'address': '123 Main St',
            'username': 'john_doe',
            'email': 'john@example.com',
            'password': 'securepassword'
        }
        response = self.client.post(reverse('create_user'), data=form_data)
        self.assertEqual(response.status_code, 200)  

    def test_create_user_form_empty_data(self):
        form_data = {
            'user_type': '',
            'name': '',
            'lastname': '',
            'phoneNumber': '',
            'address': '',
            'username': '',
            'email': '',
            'password': ''
        }
        response = self.client.post(reverse('create_user'), data=form_data)
        self.assertEqual(response.status_code, 200) 

    def test_create_user_view(self):
        url = reverse('create_user')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, 'Crear cuenta')


