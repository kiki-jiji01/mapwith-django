from django.db import models

# Create your models here.
class Countries(models.Model):
    country_name = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    
    def __str__(self):
        return self.country_name