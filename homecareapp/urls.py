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
    path('login', views.user_login, name="login"),     
    path('logout', views.user_logout, name='logout'),
    path('register', views.register, name='register'),
    path("api/add_serviceprovider_fovourite/<int:user_id>", api.add_serviceprovider_fovourite, name="add_serviceprovider_fovourite"),    
    
]
