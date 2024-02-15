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
        fields = ('first_name', 'last_name', 'mobile', 'date_of_birth', 'user_type')
        widgets = {
            "first_name" : getTextInput('first name?'),
            "last_name"  : getTextInput('Last Name?'),
            "mobile" : getTextInput('mobile?'), 
            "date_of_birth" : getTextInput('date_of_birth?'),
            "user_type" : getTextInput('user_type?')
        }          
        
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        mobile = cleaned_data.get("mobile")
        date_of_birth = cleaned_data.get("date_of_birth")
        user_type = cleaned_data.get("user_type")
        
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
        
        if not user_type:
            raise ValidationError("User Type cannot be blank")        