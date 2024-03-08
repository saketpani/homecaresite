# I wrote this code

from django import forms
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *
from .helper import *

class UserForm(ModelForm):
    '''
    User Form
    '''    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            "username" : getTextInput('username?'),
            "email" : getTextInput('Email Address?'), 
            "password" : PasswordInput(attrs = { 'class' : 'form-control' })           
            }    
        
class UserProfileForm(ModelForm):
    '''
    User Profile Form
    '''            
    class Meta:
        model = AppUser
        fields = ('first_name', 'last_name', 'mobile', 'date_of_birth')
        widgets = {
            "first_name" : getTextInput('first name?'),
            "last_name"  : getTextInput('Last Name?'),
            "mobile" : getTextInput('mobile?'), 
            "date_of_birth" : getTextInput('date_of_birth?'),            
        }          
        
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        mobile = cleaned_data.get("mobile")
        date_of_birth = cleaned_data.get("date_of_birth")    
        
        if not first_name:
            raise ValidationError("first name cannot be blank")
        else:            
            if len(first_name) > 256:
                raise ValidationError("Maximum characters allowed for first name is 256.")
                
        if not last_name:
            raise ValidationError("last name cannot be blank")
        else:            
            if len(last_name) > 256:
                raise ValidationError("Maximum characters allowed for last name is 256.") 
            
        if not mobile:
            raise ValidationError("mobile cannot be blank")
        else:            
            if len(mobile) > 50:
                raise ValidationError("Maximum characters allowed for mobile is 50.") 
            if not mobile.isdigit():
                raise ValidationError("mobile phone should be numbers only.") 
            
        if not date_of_birth:
            raise ValidationError("Date of birth cannot be blank")
        
class UserProfileEditForm(ModelForm):
    '''
    User Profile Edit Form
    '''        
    class Meta:
        model = AppUser
        fields = ('first_name', 'last_name', 'mobile', 'date_of_birth')
        widgets = {
            "first_name" : getReadOnlyTextInput('First Name?'),
            "last_name"  : getReadOnlyTextInput('Last Name?'),
            "mobile" : getTextInput('mobile?'),
            "date_of_birth" : getReadOnlyTextInput('Date of birth?')                  
        }    
        
    def clean(self):
        cleaned_data = super().clean()
        mobile = cleaned_data.get("mobile")
        if not mobile:
            raise ValidationError("mobile cannot be blank")
        else:            
            if len(mobile) > 50:
                raise ValidationError("Maximum characters allowed for mobile is 50.") 
            if not mobile.isdigit():
                raise ValidationError("mobile phone should be numbers only.") 

class ServiceProviderForm(ModelForm):
    '''
    Service Provider Profile Form
    '''            
    image = forms.ImageField(required=False)
    class Meta:
        model = ServiceProvider
        fields = ('title', 'summary', 'details', 'website_url', 'services', 
                  'email', 'contact_number1', 'contact_number2',
                  'address_line1', 'address_line2', 'city', 'pin', 'landmark', 'image')         
        
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        summary = cleaned_data.get("summary")
        website_url = cleaned_data.get("website_url")
        email = cleaned_data.get("email")
        contact_number1 = cleaned_data.get("contact_number1")
        address_line1 = cleaned_data.get("address_line1")
        city = cleaned_data.get("city")
        pin = cleaned_data.get("pin")
        
        if not title:
            raise ValidationError("title cannot be blank")
        else:            
            if len(title) > 1000:
                raise ValidationError("Maximum characters allowed for title is 256.")
                
        if not summary:
            raise ValidationError("summary cannot be blank")
        else:            
            if len(summary) > 2000:
                raise ValidationError("Maximum characters allowed for summary is 2000.")                    
            
        if not website_url:
            raise ValidationError("website url cannot be blank")  
        if not email:
            raise ValidationError("email cannot be blank")    
        if not contact_number1:
            raise ValidationError("contact_number1 cannot be blank")    
        if not address_line1:
            raise ValidationError("address_line1 cannot be blank") 
        if not city:
            raise ValidationError("city cannot be blank") 
        if not pin:
            raise ValidationError("pin cannot be blank")                