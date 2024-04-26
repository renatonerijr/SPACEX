from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class LaunchTests(APITestCase):


    def test_latest(self):

        url = reverse('launch-latest')
        response = self.client.get(url, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_next(self):

        url = reverse('launch-next')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_upcoming(self):

        url = reverse('launch-upcoming')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_past(self):

        url = reverse('launch-past')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_one(self):

        url = reverse('launch-one', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
