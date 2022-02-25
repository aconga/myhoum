from django.test import TestCase
from django.contrib.auth.models import User
from position.models import Property


class ModelsTestCase(TestCase):
    def test_post_has_address(self):
        my_user = User.objects.create(username='Testuser')
        property = Property.objects.create(
            address="1600 Amphitheatre Parkway, Mountain View, CA",
            latitude=12.12,
            longitude=12.36,
            houm=my_user
        )
        property.save()
        self.assertEqual(property.address, "1600 Amphitheatre Parkway, Mountain View, CA")