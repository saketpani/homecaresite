from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),   
    path('faq', views.faq, name="faq"),   
    path('dashboard', views.dashboard, name="dashboard"),   
    path('search', views.search, name="search"),   
    path('searchResults', views.searchResults, name="searchResults"),   
    path('login', views.user_login, name="login"),     
    path('register', views.register, name='register'),
]
