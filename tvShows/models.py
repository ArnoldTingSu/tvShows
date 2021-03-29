from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def input_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show must be at least 2 characters long!"
        if len(postData['network']) < 3:
            errors["network"] = "Network must be at least 3 characters long!"
        if len(postData['description']) == 0:
            return errors
        else:
            if len(postData['description']) < 10:
                errors["description"] = "Description must at least be 10 characters long!"
        return errors

class Show(models.Model):
    title=models.CharField(max_length=225)
    network=models.CharField(max_length=225)
    release=models.DateField()
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = ShowManager()
