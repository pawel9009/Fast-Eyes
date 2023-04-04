from django.test import Client, TestCase
from django.urls import reverse

from .models import User


class UserRegistrationTestCase(TestCase):
    def setUp(self) -> None:
        self.cl = Client()
        self.url = reverse('accounts:signup')
        self.username = 'user999',
        self.password1 = 'zaq1@WSX',
        self.password2 = 'zaq1@WSX',
        self.birth_day = 1934,
        self.sex = 'Male',
        self.ailments = 'sdadasd',
        return super().setUp()

    def test_registration(self):
        response = self.client.post(self.url, {
            'username': self.username,
            'password1': self.password1,
            'password2':  self.password2,
            'birth_day':  self.birth_day,
            'sex': self.sex,
            'ailments':  self.ailments,
        }, format='text/html')

        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username=self.username)
        self.assertIsNotNone(user)
