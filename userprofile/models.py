from django.contrib.auth.models import User
from django.db import models



class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    
    
