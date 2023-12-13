from django.db import models
from apps.categories.models import Categories
from apps.users.models import Users
# Create your models here.



#categoria
class Posts(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null = True)

    class Meta:
        managed = True
        db_table = 'posts'
        ordering = ('-created_at',)