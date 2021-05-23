from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    address=models.CharField(max_length=100)