from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=30)
    contact_picture = models.URLField(null=True)
    is_favorited = models.BooleanField(default = False)
    