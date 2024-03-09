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

import json

class RegisterViewTest(TestCase):        
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_register_page(self):   
        # arrange           
        register_url = reverse('register')           
        # act
        response = self.client.get(register_url)        
        # assert
        self.assertEquals(response.status_code, 200)
    def test_register_returns_register_template_when_ok(self):   
        '''
        Test that register returns register template on successful response
        '''
        # arrange          
        register_url = reverse('register')      
        
        # act
        response = self.client.get(register_url)
        
        # assert        
        self.assertTemplateUsed(response, 'homecareapp/register.html')              
                    
class UserLoginViewTest(TestCase):        
    '''
    Test class for User Login View implementation
    '''                
    def setUp(self):  
        '''
        Initialization before the tests executed.
        '''                                  
        user = UserFactory.create(pk = 1, username='john', email = 'john@j.com', password='john123')
        AppUserFactory.create(pk = 1, first_name = 'John', last_name = 'Doe', mobile = '7827222', user = user)                            
        
    def tearDown(self):
        '''
        Method called after the tests are executed.
        '''
        User.objects.all().delete()
        AppUser.objects.all().delete()
        UserFactory.reset_sequence(0)    
        AppUserFactory.reset_sequence(0)          
    
    def test_user_login_returns_ok(self):   
        '''
        Test that login returns OK 200 status on successful response
        '''  
        # arrange           
        login_url = reverse('login')   
        
        # act
        response = self.client.get(login_url)
        
        # assert
        self.assertEquals(response.status_code, 200)        
        
    def test_user_login_returns_login_template_when_ok(self):   
        '''
        Test that user_login returns login template on successful response
        '''
        # arrange           
        login_url = reverse('login') 
        
        # act
        response = self.client.get(login_url)
        
        # assert        
        self.assertTemplateUsed(response, 'homecareapp/login.html')              
        
    def test_login_returns_ok_when_authenticated(self):        
        '''
        Test that user_login returns 200 when the form is submitted with 
        valid credentials and authenticated
        '''        
        # arrange           
        login_url = reverse('login') 
        
        # act
        payload = json.dumps({'username':'john', 'password': "john2"})
        content_type = 'application/json'        
        response = self.client.post(login_url, payload, content_type=content_type)        
        
        # assert
        self.assertEquals(response.status_code, 200)      
        
    def test_login_returns_login_when_authentication_fails(self):  
        '''
        Test that user_login returns login template when the form is submitted with 
        invalid credentials and authentication fails
        '''            
        # arrange           
        login_url = reverse('login') 
        
        # act
        payload = json.dumps({'username':'invaliduser', 'password': "invalid"})
        content_type = 'application/json'        
        response = self.client.post(login_url, payload, content_type=content_type)        
        
        # assert
        self.assertTemplateUsed(response, 'homecareapp/login.html')    
           
        # arrange       
        dashboard_url = reverse('dashboard', args=['2']) 
        
        # act
        response = self.client.get(dashboard_url)
        
        # assert
        self.assertEquals(response.status_code, 302)   

class UserLogoutViewTest(TestCase):        
    '''
    Test class for logout View implementation
    '''                    
    def setUp(self):
        '''
        Initialization before the tests executed.
        '''                                 
        user = UserFactory.create(pk = 1, username='john', email = 'john@j.com', password='john2')
        AppUserFactory.create(pk = 1, first_name = 'John', last_name = 'Doe', mobile = '7827222', user = user)                            
        
    def tearDown(self):
        '''
        Method called after the tests are executed.
        '''
        User.objects.all().delete()
        AppUser.objects.all().delete()
        UserFactory.reset_sequence(0)    
        AppUserFactory.reset_sequence(0)          
    
    def test_logout_returns_redirects_when_logged_out_successfully(self):   
        '''
        Test that logout returns redirects when logged out successfully
        '''
        # arrange   
        self.client.force_login(User.objects.get_or_create(username='john')[0])
        user_post_url = reverse('logout')   
        
        # act
        response = self.client.get(user_post_url)
        
        # assert
        self.assertEquals(response.status_code, 302)                
                
class DashboardViewTest(TestCase):        
    '''
    Test class for Dashboard View implementation
    '''                
    def setUp(self):  
        '''
        Initialization before the tests executed.
        '''                                  
        user = UserFactory.create(pk = 1, username='john', email = 'john@j.com', password='john123')
        AppUserFactory.create(pk = 1, first_name = 'John', last_name = 'Doe', mobile = '7827222', user = user)                            
        
    def tearDown(self):
        '''
        Method called after the tests are executed.
        '''
        User.objects.all().delete()
        AppUser.objects.all().delete()
        UserFactory.reset_sequence(0)    
        AppUserFactory.reset_sequence(0)          
    
    def test_dashbaord_returns_ok(self):   
        '''
        Test that login returns OK 200 status on successful response
        '''  
        # arrange           
        self.client.force_login(User.objects.get_or_create(username='john')[0])
        dashboard_url = reverse('dashboard', args=['1']) 
        
        # act        
        response = self.client.get(dashboard_url) 
        
        # assert
        self.assertEquals(response.status_code, 200)        
        
    def test_user_dashbaord_returns_dashbaord_template_when_ok(self):   
        '''
        Test that dashbaord returns dashbaord template on successful response
        '''
        # arrange           
        self.client.force_login(User.objects.get_or_create(username='john')[0])
        dashboard_url = reverse('dashboard', args=['1']) 
        
        # act
        response = self.client.get(dashboard_url)
        
        # assert        
        self.assertTemplateUsed(response, 'homecareapp/dashboard.html')              
        
    
