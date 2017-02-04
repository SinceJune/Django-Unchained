from django.db import models
from article.models import Article


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=32)
    article = models.ManyToManyField(Article, blank=True)
