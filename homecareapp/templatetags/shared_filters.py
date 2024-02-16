from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='split')
@stringfilter
def split(value, key):
    '''
    splits the string
    '''
    return value.split(key)