# I wrote this code

from rest_framework.serializers import ModelSerializer
from .models import *

class ServiceProviderFavouriteSerializer(ModelSerializer):
    '''
    Serializer class for User model
    '''
    class Meta:
        '''
        Metadata definition for Serializer
        '''
        model = User
        fields = ['user', 'service_provider']
        
        
# end of code I wrote