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


class SearchViewTest(TestCase):
    '''
    Test class for Search User View implementation
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
        ServiceProviderFactory.create(pk=2, title='care service2', summary='care service summary2', details="care service summary",
                                      website_url='www.cs2.com', services='home care2', email="test2@test.com", rating='4',
                                      contact_number1='3688896397', contact_number2="3658796393",
                                      address_line1='address line1', address_line2='address line2', city="city", pin="637630", landmark="landmark")

    def tearDown(self):
        '''
        Method called after the tests are executed.
        '''
        User.objects.all().delete()
        AppUser.objects.all().delete()
        ServiceProvider.objects.all().delete()
        UserFactory.reset_sequence(0)
        ServiceProviderFactory.reset_sequence(0)

    def test_search_returns_badrequest_when_submitted_with_invalid_input(self):
        # arrange
        self.client.force_login(User.objects.get_or_create(username='john')[0])
        search_url = reverse('search')
        payload = json.dumps({'search_input': ''})
        content_type = 'application/json'

        # act
        response = self.client.post(
            search_url, payload, content_type=content_type)

        # assert
        self.assertEquals(response.status_code, 400)
     
# end of code I wrote
