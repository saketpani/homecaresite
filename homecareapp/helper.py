# I wrote this code

from django.forms import TextInput, Textarea
import random

def getTextInput(placeholderValue = ''):
    '''
    helper method to return TextInput instance
    '''
    if placeholderValue != '':
        return TextInput(attrs = { 'class' : 'form-control', 'placeholder' : placeholderValue })
    else:
        return TextInput(attrs = { 'class' : 'form-control' })      

def getReadOnlyTextInput(placeholderValue):
    '''
    helper method to return readonly TextInput instance
    '''
    return TextInput(attrs = { 'class' : 'form-control', 'placeholder' : placeholderValue, 'readonly': 'readonly' })
        
def getTextArea(placeholderValue, rows):
    '''
    helper method to return TextInput instance
    '''
    return Textarea(attrs = { 'class' : 'form-control mb-2', 'placeholder' : placeholderValue, 'rows': rows })

def greeting():
    '''
    Helper method to return greeting
    '''
    return  random.choice(['Hi', 'Hello', 'Hey'])

def greeting_message():
    '''
    helper method to return greetings message
    '''
    return  random.choice(
        ["How are you today", 
         "What's up", 
         'How was the day so far', 
         'How is life']
        )

# end of code I wrote    