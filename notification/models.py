from django.db import models

# Create your models here.

class notify(models.Model):
    name = models.CharField(max_length=32)
    message =  models.TextField()
    date = models.DateField()
    def __str__(self):
     return self.name

