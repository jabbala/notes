from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=5000)
    likes = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
