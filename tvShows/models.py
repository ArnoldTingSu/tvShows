from django.db import models

# Create your models here.

class Show(models.Model):
    title=models.CharField(max_length=225)
    network=models.CharField(max_length=225)
    release=models.DateField()
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
