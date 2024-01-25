from django.test import TestCase
from django.urls import reverse

# Home View Tests
class HomeViewTest(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_home_page(self):   
        # arrange           
        home_url = reverse('index')           
        # act
        response = self.client.get(home_url)        
        # assert
        self.assertEquals(response.status_code, 200)

# About View Tests
class AboutViewTest(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_home_page(self):   
        # arrange           
        about_url = reverse('about')           
        # act
        response = self.client.get(about_url)        
        # assert
        self.assertEquals(response.status_code, 200)

# FAQ View Tests
class FAQViewTest(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_home_page(self):   
        # arrange           
        faq_url = reverse('faq')           
        # act
        response = self.client.get(faq_url)        
        # assert
        self.assertEquals(response.status_code, 200)
                                