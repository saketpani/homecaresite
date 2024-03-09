from django.test import TestCase
from django.urls import reverse
from .helper import *

from rest_framework.test import APITestCase
from rest_framework import status

from .model_factories import *
from .serializers import *
from .helper import *
from .forms import *

from django.forms import TextInput, Textarea
from django.contrib.auth import authenticate, login

# Home View Tests
class HomeViewTest(TestCase):
    def setUp(self):
        '''
        Initialization before the tests executed.
        '''   
        PageContentFactory.create(pk = 1, title = 'Home', summary = 'summary', 
                                category='home',
                                content1Title = "Header 1", content1Description = "content1 description",
                                content2Title = "Header 2", content2Description = "content2 description",
                                content3Title = "Header 3", content3Description = "content3 description",)
    def tearDown(self):
        '''
        Method called after the tests are executed.
        '''
        PageContent.objects.all().delete()
        PageContentFactory.reset_sequence(0)    
    def test_home_page(self):   
        # arrange           
        home_url = reverse('index')           
        # act
        response = self.client.get(home_url)        
        # assert
        self.assertEquals(response.status_code, 200)
    def test_home_returns_index_template_when_ok(self):   
        '''
        Test that home returns index template on successful response
        '''
        # arrange          
        home_url = reverse('index')      
        
        # act
        response = self.client.get(home_url)
        
        # assert        
        self.assertTemplateUsed(response, 'homecareapp/index.html')              
        
    def test_home_view_returns_home_category_item_when_ok(self):   
        '''
        Test that Home view returns home content on successful response
        '''
        # arrange          
        home_url = reverse('index')     
        
        # act
        response = self.client.get(home_url)       
        
        # assert        
        self.assertTrue(response.context['page_content'].category == 'home')        
        
    def test_home_view_returns_home_content_when_ok(self):   
        '''
        Test that Home view returns home content on successful response
        '''
        # arrange          
        home_url = reverse('index')     
        
        # act
        response = self.client.get(home_url)       
        
        # assert        
        self.assertTrue(response.context['page_content'].title == 'Home')
        self.assertTrue(response.context['page_content'].summary == 'summary')                

# About View Tests
class AboutViewTest(TestCase):
    def setUp(self):
        '''
        Initialization before the tests executed.
        '''           
        PageContentFactory.create(pk = 1, title = 'About us', summary = 'summary of about us', 
                                category='about',
                                content1Title = "Header 1", content1Description = "content1 description",
                                content2Title = "Header 2", content2Description = "content2 description",
                                content3Title = "Header 3", content3Description = "content3 description",)
    def tearDown(self):
        '''
        Method called after the tests are executed.
        '''       
        PageContent.objects.all().delete()
        PageContentFactory.reset_sequence(0)    
    def test_about_page(self):   
        # arrange           
        about_url = reverse('about')           
        # act
        response = self.client.get(about_url)        
        # assert
        self.assertEquals(response.status_code, 200)
    def test_about_returns_about_template_when_ok(self):   
        '''
        Test that About returns About template on successful response
        '''
        # arrange          
        about_url = reverse('about')    
        
        # act
        response = self.client.get(about_url)    
        
        # assert        
        self.assertTemplateUsed(response, 'homecareapp/about.html')          

    def test_about_view_returns_about_category_item_when_ok(self):   
        '''
        Test that About view returns about content on successful response
        '''
        # arrange          
        about_url = reverse('about')    
        
        # act
        response = self.client.get(about_url)       
        
        # assert        
        self.assertTrue(response.context['page_content'].category == 'about')        
        
    def test_about_view_returns_about_content_when_ok(self):   
        '''
        Test that About view returns about content on successful response
        '''
        # arrange          
        about_url = reverse('about')    
        
        # act
        response = self.client.get(about_url)       
        
        # assert        
        self.assertTrue(response.context['page_content'].title == 'About us')
        self.assertTrue(response.context['page_content'].summary == 'summary of about us')                
        
# FAQ View Tests
class FAQViewTest(TestCase):
    def setUp(self):
        '''
        Initialization before the tests executed.
        '''           
        FAQFactory.create(pk = 1, question = 'faq question', answer = 'faq answer')
    def tearDown(self):
        '''
        Method called after the tests are executed.
        '''        
        FAQ.objects.all().delete()         
        FAQFactory.reset_sequence(0)    
    def test_faq_page_returns_ok(self):   
        # arrange           
        faq_url = reverse('faq')           
        # act
        response = self.client.get(faq_url)        
        # assert
        self.assertEquals(response.status_code, 200)
    def test_faq_returns_faq_template_when_ok(self):   
        '''
        Test that FAQ returns FAQ template on successful response
        '''
        # arrange          
        faq_url = reverse('faq')    
        
        # act
        response = self.client.get(faq_url)    
        
        # assert        
        self.assertTemplateUsed(response, 'homecareapp/faq.html')      
    
    def test_faq_returns_faq_list_when_ok(self):   
        '''
        Test that FAQ returns FAQ template on successful response
        '''
        # arrange    
        FAQFactory.create(pk = 2, question = 'faq question 2', answer = 'faq answer 2')      
        faq_url = reverse('faq')    
        
        # act
        response = self.client.get(faq_url)    
        
        # assert        
        self.assertTrue(len(response.context['faq_results']) == 2)
        
    def test_faq_returns_faq_list_when_another_faq_added_ok(self):   
        '''
        Test that FAQ returns FAQ template on successful response
        '''
        # arrange          
        faq_url = reverse('faq')    
        
        # act
        response = self.client.get(faq_url)    
        
        # assert        
        self.assertTrue(len(response.context['faq_results']) == 1)        
                                