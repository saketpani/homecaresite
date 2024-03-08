import factory
from factory.django import DjangoModelFactory
from .models import *
        
class UserFactory(DjangoModelFactory):
    '''
    UserFactory class used for unit testing
    '''        
    class Meta:
        model = User

class AppUserFactory(DjangoModelFactory):
    '''
    AppUserFactory class used for unit testing
    '''
    first_name = ""
    last_name = ""    
    mobile = ""
    date_of_birth = ""
    user_type = ""
            
    user = factory.SubFactory(UserFactory)    

    class Meta:
        model = AppUser    
        
class FAQFactory(DjangoModelFactory):
    '''
    FAQFactory class used for unit testing
    '''
    question = ""
    answer = ""            

    class Meta:
        model = FAQ            

class PageContentFactory(DjangoModelFactory):
    '''
    PageContentFactory class used for unit testing
    '''
    title = ""
    summary = ""
    category = ""

    content1Title = ""
    content1Description = ""
    content2Title = ""
    content2Description = ""
    content3Title = ""
    content3Description = ""
           

    class Meta:
        model = PageContent            

class ServiceProviderFactory(DjangoModelFactory):
    '''
    ServiceProviderFactory class used for unit testing
    '''
    title = ""
    summary = ""
    details = ""

    website_url = ""
    rating = ""
    services = ""
    email = ""
    contact_number1 = ""
    contact_number2 = ""
    
    address_line1 = ""
    address_line2 = ""
    city = ""
    pin = ""
    landmark = ""    
           

    class Meta:
        model = ServiceProvider     
        
class ServiceProvider_FavouriteFactory(DjangoModelFactory):
    '''
    ServiceProvider_FavouriteFactory class used for unit testing
    '''
    user = None
    service_provider = None         

    class Meta:
        model = ServiceProvider_Favourite                 


class ProviderUserFactory(DjangoModelFactory):
    '''
    ProviderUserFactory class used for unit testing
    '''
    user_type = ""
    user = None
    provider = None
    class Meta:
        model = ProviderUser                 
