from django.db import models

# Create your models here.

class ImageUpload(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image/')
