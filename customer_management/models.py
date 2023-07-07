from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField (max_length=32)
    email = models.EmailField()
    contacts = models.CharField (max_length=32)
    location= models.CharField (max_length=32)

    
    def __str__(self):
        return self.name
