from django.db import models

# Create your models here.
class FAQ(models.Model):
    '''
    FAQ Model class
    '''            
    question = models.CharField(max_length=256, null=False, blank=False)
    answer = models.CharField(max_length=4000)                    
    def __str__(self):
        return self.question + ": " + self.answer