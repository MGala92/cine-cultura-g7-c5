from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(AbstractUser):
    # role = models.CharField(max_length=10)
   
    class Meta:
        managed = True
        db_table = 'users'