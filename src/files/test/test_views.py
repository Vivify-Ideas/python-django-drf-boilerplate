import mock
from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
from django.core.files import File
from unittest.mock import patch

from src.users.test.factories import UserFactory

fake = Faker()


class TestFileUpload(APITestCase):
    """
    Tests /file/upload endpoint
    """
    def setUp(self):
        self.user = UserFactory()
        self.url = reverse('file-upload')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')

    def test_upload_without_params(self):
        response = self.client.post(self.url, {}, format='multipart')
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_upload_without_file(self):
        response = self.client.post(self.url, {'description': 'some desc', 'file': ''}, format='multipart')
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('django.core.files.storage.FileSystemStorage.save')
    def test_successfull_upload(self, mock_save):
        mock_save.return_value = 'file.txt'

        response = self.client.post(
            self.url,
            {
                'description': 'some desc',
                'file': mock.MagicMock(spec=File),
            },
            format='multipart'
        )
        eq_(response.status_code, status.HTTP_201_CREATED)
        mock_save.assert_called_once()
