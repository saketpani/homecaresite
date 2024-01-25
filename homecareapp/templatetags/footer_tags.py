
# I wrote this code

import datetime 
from django import template  

register = template.Library()  

@register.simple_tag 
def todays_date():     
    '''
    Tag to display date
    '''
    return datetime.datetime.now().strftime("%d %b, %Y") 

@register.simple_tag 
def author():  
    '''
    Tag to display Author 
    '''
    return 'Author: Saket'

@register.simple_tag 
def note():  
    '''
    Tag to display note
    '''    
    return 'Images are from www.pexels.com'

# end of code I wrote    