from django.db import models

# Create your models here.
from django.db import models
# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    username= models.CharField(max_length=150, unique=True)
