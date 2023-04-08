from django.db import models

# Create your models here.
class UrlDataset(models.Model):
    Name = models.CharField(max_length=20)
    Url = models.CharField(max_length=30)
    Type = models.CharField(max_length=20)