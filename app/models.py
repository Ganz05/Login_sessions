from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField()
    address=models.TextField()
