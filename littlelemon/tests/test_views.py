from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = MenuItem.objects.create(title="Pizza", price=10, inventory=50)
        self.item2 = MenuItem.objects.create(title="Burger", price=5, inventory=20)

    def test_get_all_items(self):
        response = self.client.get('/restaurant/menu/')
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)