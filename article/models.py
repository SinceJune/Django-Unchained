from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
