from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponseNotFound
import json

from .models import *
from.serializers import *

@api_view(['POST'])
def add_serviceprovider_fovourite(request, user_id):
    '''
    Add favourite
    '''
    if request.method == 'POST': 
        print('user id: ' + str(user_id))
        print('api called')
        
        # try:
        #     user = User.objects.get(pk=user_id) 
        # except User.DoesNotExist:
        #     return HttpResponseNotFound("User not found.")   
                                                              
        provider_id = request.data['service_provider']                
        
        serviceprovider_favourite = ServiceProvider_Favourite(user = User.objects.get(pk=request.user.id), 
                                         service_provider = ServiceProvider.objects.get(pk=provider_id))
            
                
        serviceprovider_favourite.save()
        response_data = {}
        response_data['result'] = 'success'
        
        return Response(json.dumps(response_data), content_type="application/json", status=status.HTTP_200_OK)
    