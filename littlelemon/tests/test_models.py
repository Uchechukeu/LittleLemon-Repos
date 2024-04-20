from django.test import TestCase, Client
from django.urls import reverse
import json
from restaurant.models import menu
from restaurant.views import *


#Test case class
#the test below runs at restaurant/test.py file
class menuTest(TestCase):
    def test_get_item(self):
        item = menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), 'IceCream : 80')
