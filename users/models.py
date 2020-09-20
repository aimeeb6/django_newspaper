from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank= True)
    #null allows the database to store null 
    #blank allows the form to accept a blank field
