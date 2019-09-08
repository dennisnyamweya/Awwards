from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    info = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/',blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']