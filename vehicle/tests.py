from rest_framework import status
from rest_framework.test import APITestCase

from vehicle.models import Car


class VehicleTestCase(APITestCase):

    def setUp(self):
        pass

    def test_create_car(self):
        """Тестирование создания машин"""

        data = {
            "title": "Test",
            "description": "Test"
        }
        response = self.client.post(
            '/cars/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 1, 'milage': [], 'title': 'Test', 'description': 'Test', 'owner': None}
        )

        self.assertTrue(
            Car.objects.all().exists()
        )

    def test_list_car(self):
        """Тестирование вывода списка машин"""

        response = self.client.get(
            '/cars/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

