from django.test import TestCase, Client
from django.urls import reverse
import json
from restaurant.models import menu
from restaurant.views import *


#a new test case to chech post call to the menu endpoint
class menupostTest(TestCase):
    def test_post_item(self):
        self.Client = Client()
        self.menu = reverse('menu')
        response = self.Client.post(self.menu, {"title" : "Fried_chicken", "price" : "7.00", "inventory": "10"})
        self.assertEquals(response.status_code, 201)

#the test case below works but not in this folder. It works at reastaurant/test.py file
#this testcase ca now run in this folder. Ensure to run test in the terminal this way: python manage.py test tests
class menuTest(TestCase):  
    def test_get_item(self):
        self.Client = Client()
        self.menu_url = reverse('menu')
        response = self.Client.get(self.menu_url)
        self.assertEquals(response.status_code, 200)
        

#Test case class
#the test case below did not work
class menuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu_url = reverse('menu')
        
    def menu_Object_get(self):
        response = self.Client.get(self.menu_url)
        
        self.assertEquals(response.status_code, 200)
        
        