# I wrote this code
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

# Helper Tests Starts


class HelperTest(TestCase):
    '''
    Test class for Helper methods
    '''

    def test_getTextInput_With_Placeholder_Input(self):
        '''
        Testing getTextInput with placeholder input
        '''
        text_input = getTextInput('title')
        self.assertIsInstance(text_input, TextInput)

    def test_getTextInput_With_Placeholder_Input_Returns_Correct_Placeholder_Value(self):
        '''
        Testing getTextInput with placeholder input
        '''
        # arrange
        placeholder_value = 'title'

        # act
        text_input = getTextInput(placeholder_value)

        # assert
        self.assertEqual(text_input.attrs['placeholder'], placeholder_value)

    def test_getTextInput_With_Placeholder_Input_Returns_Correct_Class_Value(self):
        '''
        Testing getTextInput with placeholder input
        '''
        # arrange
        placeholder_value = 'title'
        class_value = 'form-control'

        # act
        text_input = getTextInput(placeholder_value)

        # assert
        self.assertEqual(text_input.attrs['class'], class_value)

    def test_getTextInput_With_Empty_Placeholder_Input(self):
        '''
        Testing getTextInput with placeholder input
        '''
        # arrange
        placeholder_value = ''

        # act
        text_input = getTextInput(placeholder_value)

        # assert
        self.assertIsInstance(text_input, TextInput)

    def test_getTextInput_With_Empty_Placeholder_Input_Returns_Correct_Class_Value(self):
        '''
        Testing getTextInput with placeholder input
        '''
        # arrange
        placeholder_value = ''
        class_value = 'form-control'

        # act
        text_input = getTextInput(placeholder_value)

        # assert
        self.assertEqual(text_input.attrs['class'], class_value)

    def test_getReadOnlyTextInput_With_Placeholder_Input(self):
        '''
        Testing getReadOnlyTextInput with placeholder input
        '''
        text_input = getReadOnlyTextInput('title')
        self.assertIsInstance(text_input, TextInput)

    def test_getReadOnlyTextInput_With_Placeholder_Input_Returns_Correct_Placeholder_Value(self):
        '''
        Testing getReadOnlyTextInput with placeholder input
        '''
        # arrange
        placeholder_value = 'title'

        # act
        text_input = getReadOnlyTextInput(placeholder_value)

        # assert
        self.assertEqual(text_input.attrs['placeholder'], placeholder_value)

    def test_getReadOnlyTextInput_With_Empty_Placeholder_Input_Returns_Correct_ReadOnly_Value(self):
        '''
        Testing getReadOnlyTextInput with placeholder input
        '''
        # arrange
        placeholder_value = 'title'

        # act
        text_input = getReadOnlyTextInput(placeholder_value)

        # assert
        self.assertEqual(text_input.attrs['readonly'], 'readonly')

    def test_getTextArea_With_Placeholder_Input(self):
        '''
         Testing getReadOnlyTextInput with placeholder and rows input returns Textarea instance
        '''
        # arrange
        placeholder_value = 'description'
        rows = '4'

        # act
        text_area = getTextArea(placeholder_value, rows)

        # assert
        self.assertIsInstance(text_area, Textarea)

    def test_getTextArea_With_Placeholder_Input_Returns_Correct_Placeholder_Value(self):
        '''
         Testing getReadOnlyTextInput with placeholder and rows input returns Textarea with
        correct placeholder value
        '''
        # arrange
        placeholder_value = 'description'
        rows = '4'

        # act
        text_area = getTextArea(placeholder_value, rows)

        # assert
        self.assertEqual(text_area.attrs['placeholder'], placeholder_value)

    def test_getTextArea_With_Valid_Input_Returns_Textarea_With_Correct_Rows_Value(self):
        '''
        Testing getReadOnlyTextInput with placeholder and rows input has correct rows
        '''
        # arrange
        placeholder_value = 'description'
        rows = '4'

        # act
        text_area = getTextArea(placeholder_value, rows)

        # assert
        self.assertEqual(text_area.attrs['rows'], rows)


# Helper Tests Ends

# API Tests Starts


class UserListAPITest(APITestCase):

    '''
    Test class for user_list API implementation
    '''

    def setUp(self):
        '''
        Initialization before the tests executed.
        '''
        user = UserFactory.create(
            pk=1, username='john', email='john@j.com', password='john2')
        AppUserFactory.create(pk=1, first_name='John',
                              last_name='Doe', mobile='7827222', user=user)
        ServiceProviderFactory.create(pk=1, title='care service1', summary='care service summary', details="care service summary",
                                      website_url='www.cs.com', services='home care', rating='4', email="test@test.com",
                                      contact_number1='3688796397', contact_number2="3688796393",
                                      address_line1='address line1', address_line2='address line2', city="city", pin="637630", landmark="landmark")

    def tearDown(self):
        '''
        Method called after the tests are executed.
        '''
        User.objects.all().delete()
        AppUser.objects.all().delete()
        ServiceProvider.objects.all().delete()
        UserFactory.reset_sequence(0)
        AppUserFactory.reset_sequence(0)
        ServiceProviderFactory.reset_sequence(0)

    def test_add_serviceprovider_fovourite_returns_success(self):
        '''
        Testing add_serviceprovider_fovourite() API returns success HTTP Status Code 200 api with valid url is called
        '''
        # arrange : preprare the data
        url = reverse('add_serviceprovider_fovourite', args=['1'])

        # act : make the call to API action method
        self.client.force_login(User.objects.get_or_create(username='john')[0])
        response = self.client.post(url,  
        data=json.dumps({
            'service_provider': 1
        }),content_type='application/json',)

        # assert : Check the condition
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# API Tests Ends


# end of code I wrote
