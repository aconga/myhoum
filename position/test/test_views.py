
from datetime import datetime, timedelta
from position.models import Property

from django.urls import include, path, reverse
from rest_framework import status

from django.test import TestCase
import json
from rest_framework.test import APIClient
from rest_framework import status

from django.contrib.auth.models import User


class PropertyTestCase(TestCase):

    def setUp(self):
        user = User(
            email='testing_login@acongadev.com',
            first_name='Testing',
            last_name='Testing',
            username='testing_login'
        )
        user.set_password('admin123')
        user.save()

        client = APIClient()
        response = client.post(
                '/account/login/', {
                'email': 'testing_login@acongadev.com',
                'password': 'admin123',
                'username': 'testing_login'
            },
            format='json'
        )

        result = json.loads(response.content)
        self.access_token = result['token']
        self.user = user
    
    def test_create_property(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)
        test_address = {'address': "1600 Amphitheatre Parkway, Mountain View, CA"}
        response = client.post('/api/propertys/', test_address, format='json')
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('latitude', result)
        self.assertIn('longitude', result)
    
    def test_update_property(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.access_token)
        start_date = datetime.now()
        # create property
        test_address = {'address': "1600 Amphitheatre Parkway, Mountain View, CA"}
        response = client.post('/api/propertys/', test_address, format='json')
        property = Property.objects.all().first()
        test_finish_date = {'finish_date': "2022-02-25T11:47:04.862649-05:00"}
        response_up = client.put(f'/api/propertys/{property.pk}/', test_finish_date, format='json')
        result = json.loads(response_up.content)
        self.assertEqual(response_up.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get("finish_date"), "2022-02-25T11:47:04.862649-05:00")