from django.db import models
from django.db import models


# Create your models here.

class Phone(models.Model):
    name         = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=11, null=False)
    location     = models.CharField(max_length=100)

