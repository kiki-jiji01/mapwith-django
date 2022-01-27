from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Countries(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="countries")
    country_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    country_image = models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.country_name