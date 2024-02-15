import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserType(models.Model):
    user_type = models.CharField(max_length=50, null=False, blank=False) 
    def __str__(self):
        return self.user_type
    
class AppUser(models.Model):
    '''
    Application User Model class. Holds the data for a user 
    '''    
    # use the user table provided by authentication system
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # User profile data
    first_name = models.CharField(max_length=256, null=False, blank=False)
    last_name = models.CharField(max_length=256, null=False, blank=False)
    date_of_birth = models.DateField(null=False)
    mobile = models.CharField(max_length=50, null=True, blank=True)    
    date_created = models.DateField(default=datetime.date.today)    
    user_type = models.OneToOneField(UserType, on_delete=models.CASCADE)
        
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
        
class PageContent(models.Model):
    '''
    Page Content Model class
    '''            
    title = models.CharField(max_length=256, null=False, blank=False)
    summary = models.CharField(max_length=1000)
    category = models.CharField(max_length=256, null=False, blank=False)
    
    content1Title = models.CharField(max_length=256, null=False, blank=False)
    content1Description = models.CharField(max_length=1000)
    content2Title = models.CharField(max_length=256, null=False, blank=False)
    content2Description = models.CharField(max_length=1000) 
    content3Title = models.CharField(max_length=256, null=False, blank=False)
    content3Description = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.title
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['category'], name='unique_category')
        ]

class CareService(models.Model):
    code = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    
    def __str__(self):
        return self.code
    
class ServiceProvider(models.Model):
    title = models.CharField(max_length=1000, null=False, blank=False)
    summary = models.CharField(max_length=2000)
    details = models.CharField(max_length=4000, null=True, blank=True)
    website_url = models.CharField(max_length=1000, null=False, blank=False)
    rating = models.FloatField(null=True)
    services = models.CharField(max_length=4000, null=False, blank=False)
    
    email = models.CharField(max_length=1000, null=False, blank=False)
    contact_number1 = models.CharField(max_length=1000, null=False, blank=False)
    contact_number2 = models.CharField(max_length=1000, null=True, blank=True)
    
    address_line1 = models.CharField(max_length=1000, null=False, blank=False)
    address_line2 = models.CharField(max_length=1000, null=True, blank=True)
    city = models.CharField(max_length=1000, null=False, blank=False)
    pin = models.CharField(max_length=50, null=False, blank=False)
    landmark = models.CharField(max_length=1000, null=True, blank=True)
    
    image = models.ImageField(upload_to='assets/', null=True)        
        
    def __str__(self) -> str:
        return self.title