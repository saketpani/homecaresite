from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class AppUser(models.Model):
    '''
    Application User Model class. Holds the data for a user 
    '''    
    # use the user table provided by authentication system
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # User profile data
    first_name = models.CharField(max_length=256, null=False, blank=False)
    last_name = models.CharField(max_length=256, null=False, blank=False)
    mobile = models.CharField(max_length=50, null=True, blank=True)    
    date_created = models.DateField(default=datetime.date.today)
    user_type = models.CharField(max_length=20, null=False, blank=False)
        
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
class FAQ(models.Model):
    '''
    FAQ Model class
    '''            
    question = models.CharField(max_length=256, null=False, blank=False)
    answer = models.CharField(max_length=4000)                    
    def __str__(self):
        return self.question + ": " + self.answer