from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Trip(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=20)
    description = models.TextField()
    plan = models.CharField(max_length=30)
    travel_start_date = models.DateTimeField()
    travel_end_date  = models.DateTimeField()

    def __str__(self):
        return self.destination
    def get_absolute_url(self):
        return reverse('travel')    

