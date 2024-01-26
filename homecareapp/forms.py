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