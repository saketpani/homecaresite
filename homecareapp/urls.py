from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),   
    path('faq', views.faq, name="faq"),   
    path('dashboard/<int:id>', views.dashboard, name='dashboard'),    
    path('profile/<int:id>', views.profile_edit, name='profile_edit'),
    path('search', views.search, name="search"),       
    path('providerDetails/<int:id>', views.service_provider_details, name='providerDetails'),
    path('savedproviders', views.saved_provider_details, name="savedproviders"), 
    path('serviceprovideredit', views.serviceprovider, name="serviceprovidereditget"),    
    path('serviceprovideredit/<int:provider_id>', views.serviceprovider_edit, name="serviceprovidereditpost"),     
    path('login', views.user_login, name="login"),    
    path('service_provider_login', views.service_provider_login, name='service_provider_login'), 
    path('logout', views.user_logout, name='logout'),
    path('register', views.register, name='register'),    
    path('service_provider_registration', views.service_provider_registration, name='service_provider_registration'),
    path("api/add_serviceprovider_fovourite/<int:user_id>", api.add_serviceprovider_fovourite, name="add_serviceprovider_fovourite"),    
    
]
