from django.db import models

# Create your models here.

from django.db import models


class Document(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField()
    author = models.IntegerField()

    class Meta:
        ordering = ['created']