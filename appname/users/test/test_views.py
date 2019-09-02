from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
from ..models import User
from .factories import UserFactory

fake = Faker()


class TestUserListTestCase(APITestCase):
    """
    Tests /users list operations.
    """
    def setUp(self):
        self.url = reverse('user-list')
        self.user_data = model_to_dict(UserFactory.build())

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.user_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(pk=response.data.get('id'))
        eq_(user.username, self.user_data.get('username'))
        ok_(check_password(self.user_data.get('password'), user.password))


class TestUserDetailTestCase(APITestCase):
    """
    Tests /users detail operations.
    """
    def setUp(self):
        self.user = UserFactory()
        self.url = reverse('user-detail', kwargs={'pk': self.user.pk})
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')

    def test_get_request_returns_a_given_user(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_put_request_updates_a_user(self):
        new_first_name = fake.first_name()
        payload = {'first_name': new_first_name}
        response = self.client.put(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        user = User.objects.get(pk=self.user.id)
        eq_(user.first_name, new_first_name)


class TestUserSetPassword(APITestCase):
    """
    Tests /users/{id}/set_password endpoint
    """
    def setUp(self):
        self.user = UserFactory(password='password')
        self.url = reverse('user-set-password', kwargs={'pk': self.user.pk})
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')

    def test_incorect_old_password(self):
        response = self.client.post(self.url, {
            'old_password': 'asdf',
            'new_password': 'asdf'
        })
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_without_new_password_provided(self):
        response = self.client.post(self.url, {
            'old_password': 'password',
        })
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_changing_password_succeeds(self):
        response = self.client.post(self.url, {
            'old_password': 'password',
            'new_password': 'new',
        })
        eq_(response.status_code, status.HTTP_200_OK)
        eq_(response.data, {'status': 'password set'})
