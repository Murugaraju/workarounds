from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expiry(models.Model):
    user=models.OneToOneField(User, related_name='expiry_monitor',on_delete=models.CASCADE)
    expirytime=models.DateTimeField(blank=True,null=True)