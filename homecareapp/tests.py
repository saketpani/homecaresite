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

# # Home View Tests
# class HomeViewTest(TestCase):
#     def setUp(self):
#         pass
#     def tearDown(self):
#         pass
#     def test_home_page(self):   
#         # arrange           
#         home_url = reverse('index')           
#         # act
#         response = self.client.get(home_url)        
#         # assert
#         self.assertEquals(response.status_code, 200)
#     def test_home_returns_index_template_when_ok(self):   
#         '''
#         Test that home returns index template on successfull response
#         '''
#         # arrange          
#         home_url = reverse('index')      
        
#         # act
#         response = self.client.get(home_url)
        
#         # assert        
#         self.assertTemplateUsed(response, 'homecareapp/index.html')              
        

# # About View Tests
# class AboutViewTest(TestCase):
#     def setUp(self):
#         PageContentFactory.create(pk = 1, title = 'About us', summary = 'summary of about us', 
#                                 category='about',
#                                 content1Title = "Header 1", content1Description = "content1 description",
#                                 content2Title = "Header 2", content2Description = "content2 description",
#                                 content3Title = "Header 3", content3Description = "content3 description",)
#     def tearDown(self):
#         PageContent.objects.all().delete()
#     def test_about_page(self):   
#         # arrange           
#         about_url = reverse('about')           
#         # act
#         response = self.client.get(about_url)        
#         # assert
#         self.assertEquals(response.status_code, 200)
#     def test_about_returns_about_template_when_ok(self):   
#         '''
#         Test that About returns About template on successful response
#         '''
#         # arrange          
#         about_url = reverse('about')    
        
#         # act
#         response = self.client.get(about_url)    
        
#         # assert        
#         self.assertTemplateUsed(response, 'homecareapp/about.html')          

#     def test_about_view_returns_about_category_item_when_ok(self):   
#         '''
#         Test that About view returns about content on successfull response
#         '''
#         # arrange          
#         about_url = reverse('about')    
        
#         # act
#         response = self.client.get(about_url)       
        
#         # assert        
#         self.assertTrue(response.context['page_content'].category == 'about')        
        
#     def test_about_view_returns_about_content_when_ok(self):   
#         '''
#         Test that About view returns about content on successfull response
#         '''
#         # arrange          
#         about_url = reverse('about')    
        
#         # act
#         response = self.client.get(about_url)       
        
#         # assert        
#         self.assertTrue(response.context['page_content'].title == 'About us')
#         self.assertTrue(response.context['page_content'].summary == 'summary of about us')                
        
# # FAQ View Tests
# class FAQViewTest(TestCase):
#     def setUp(self):
#         FAQFactory.create(pk = 1, question = 'faq question', answer = 'faq answer')
#     def tearDown(self):
#         FAQ.objects.all().delete()
#     def test_faq_page_returns_ok(self):   
#         # arrange           
#         faq_url = reverse('faq')           
#         # act
#         response = self.client.get(faq_url)        
#         # assert
#         self.assertEquals(response.status_code, 200)
#     def test_faq_returns_faq_template_when_ok(self):   
#         '''
#         Test that FAQ returns FAQ template on successfull response
#         '''
#         # arrange          
#         faq_url = reverse('faq')    
        
#         # act
#         response = self.client.get(faq_url)    
        
#         # assert        
#         self.assertTemplateUsed(response, 'homecareapp/faq.html')      
    
#     def test_faq_returns_faq_list_when_ok(self):   
#         '''
#         Test that FAQ returns FAQ template on successfull response
#         '''
#         # arrange    
#         FAQFactory.create(pk = 2, question = 'faq question 2', answer = 'faq answer 2')      
#         faq_url = reverse('faq')    
        
#         # act
#         response = self.client.get(faq_url)    
        
#         # assert        
#         self.assertTrue(len(response.context['faq_results']) == 2)
        
#     def test_faq_returns_faq_list_when_another_faq_added_ok(self):   
#         '''
#         Test that FAQ returns FAQ template on successfull response
#         '''
#         # arrange          
#         faq_url = reverse('faq')    
        
#         # act
#         response = self.client.get(faq_url)    
        
#         # assert        
#         self.assertTrue(len(response.context['faq_results']) == 1)        
                                
                                
# # Helper Tests Starts

# class HelperTest(TestCase):
#     '''
#     Test class for Helper methods
#     '''
#     def test_getTextInput_With_Placeholder_Input(self):
#         '''
#         Testing getTextInput with placeholder input
#         '''
#         text_input = getTextInput('title')
#         self.assertIsInstance(text_input, TextInput)
        
#     def test_getTextInput_With_Placeholder_Input_Returns_Correct_Placeholder_Value(self):
#         '''
#         Testing getTextInput with placeholder input
#         '''
#         # arrange
#         placeholder_value = 'title'
        
#         # act
#         text_input = getTextInput(placeholder_value)
        
#         # assert
#         self.assertEqual(text_input.attrs['placeholder'], placeholder_value)           
    
#     def test_getTextInput_With_Placeholder_Input_Returns_Correct_Class_Value(self):
#         '''
#         Testing getTextInput with placeholder input
#         '''
#         # arrange
#         placeholder_value = 'title'
#         class_value = 'form-control'
        
#         # act
#         text_input = getTextInput(placeholder_value)
        
#         # assert
#         self.assertEqual(text_input.attrs['class'], class_value)           

#     def test_getTextInput_With_Empty_Placeholder_Input(self):
#         '''
#         Testing getTextInput with placeholder input
#         '''
#         # arrange
#         placeholder_value = ''
        
#         # act
#         text_input = getTextInput(placeholder_value)
        
#         # assert
#         self.assertIsInstance(text_input, TextInput)                      
    
#     def test_getTextInput_With_Empty_Placeholder_Input_Returns_Correct_Class_Value(self):
#         '''
#         Testing getTextInput with placeholder input
#         '''
#         # arrange
#         placeholder_value = ''
#         class_value = 'form-control'
        
#         # act
#         text_input = getTextInput(placeholder_value)
        
#         # assert
#         self.assertEqual(text_input.attrs['class'], class_value)        

#     def test_getReadOnlyTextInput_With_Placeholder_Input(self):
#         '''
#         Testing getReadOnlyTextInput with placeholder input
#         '''
#         text_input = getReadOnlyTextInput('title')
#         self.assertIsInstance(text_input, TextInput)
        
#     def test_getReadOnlyTextInput_With_Placeholder_Input_Returns_Correct_Placeholder_Value(self):
#         '''
#         Testing getReadOnlyTextInput with placeholder input
#         '''
#         # arrange
#         placeholder_value = 'title'
        
#         # act
#         text_input = getReadOnlyTextInput(placeholder_value)
        
#         # assert
#         self.assertEqual(text_input.attrs['placeholder'], placeholder_value)           
    
#     def test_getReadOnlyTextInput_With_Placeholder_Input_Returns_Correct_Class_Value(self):
#         '''
#         Testing getReadOnlyTextInput with placeholder input
#         '''
#         # arrange
#         placeholder_value = 'title'
#         class_value = 'form-control'
        
#         # act
#         text_input = getReadOnlyTextInput(placeholder_value)
        
#         # assert
#         self.assertEqual(text_input.attrs['class'], class_value)                                  
    
#     def test_getReadOnlyTextInput_With_Empty_Placeholder_Input_Returns_Correct_ReadOnly_Value(self):
#         '''
#         Testing getReadOnlyTextInput with placeholder input
#         '''
#         # arrange
#         placeholder_value = 'title'    
        
#         # act
#         text_input = getReadOnlyTextInput(placeholder_value)
        
#         # assert
#         self.assertEqual(text_input.attrs['readonly'], 'readonly')        

#     def test_getTextArea_With_Placeholder_Input(self):
#         '''
#          Testing getReadOnlyTextInput with placeholder and rows input returns Textarea instance
#         '''
#         # arrange
#         placeholder_value = 'description'
#         rows = '4'
        
#         # act
#         text_area = getTextArea(placeholder_value, rows)
        
#         # assert
#         self.assertIsInstance(text_area, Textarea)
        
#     def test_getTextArea_With_Placeholder_Input_Returns_Correct_Placeholder_Value(self):
#         '''
#          Testing getReadOnlyTextInput with placeholder and rows input returns Textarea with
#         correct placeholder value
#         '''
#         # arrange
#         placeholder_value = 'description'
#         rows = '4'
        
#         # act
#         text_area = getTextArea(placeholder_value, rows)
        
#         # assert
#         self.assertEqual(text_area.attrs['placeholder'], placeholder_value)           
    
#     def test_getTextArea_With_Valid_Input_Returns_Textarea_With_Correct_Class_Value(self):
#         '''
#         Testing getReadOnlyTextInput with placeholder and rows input returns Textarea with
#         correct class value
#         '''
#         # arrange
#         placeholder_value = 'description'
#         class_value = 'form-control mb-2'
#         rows = '4'
        
#         # act
#         text_area = getTextArea(placeholder_value, rows)
        
#         # assert
#         self.assertEqual(text_area.attrs['class'], class_value)    
        
#     def test_getTextArea_With_Valid_Input_Returns_Textarea_With_Correct_Rows_Value(self):
#         '''
#         Testing getReadOnlyTextInput with placeholder and rows input has correct rows
#         '''
#         # arrange
#         placeholder_value = 'description'
#         rows = '4'
        
#         # act
#         text_area = getTextArea(placeholder_value, rows)
        
#         # assert
#         self.assertEqual(text_area.attrs['rows'], rows)                                
    
#     def test_greeting_returns_valid_value(self):
#         '''
#         Testing greeting returns valid value
#         '''
#         # arrange
#         valid_values = ['Hi', 'Hello', 'Hey']
                
#         # act
#         value = greeting()
        
#         # assert
#         self.assertTrue(value in valid_values)      
       
#     def test_greeting_message_returns_valid_value(self):
#         '''
#         Testing greeting_message returns valid value
#         '''
#         # arrange
#         valid_values = ["How are you today", 
#          "What's up", 
#          'How was the day so far', 
#          'How is life']
                
#         # act
#         value = greeting_message()
        
#         # assert
#         self.assertTrue(value in valid_values)    
        
# # Helper Tests Ends                                