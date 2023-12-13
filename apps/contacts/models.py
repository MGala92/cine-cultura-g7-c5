from django.db import models

# Create your models here.

class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = True
        db_table = 'contacts'