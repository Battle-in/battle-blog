from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)