from django.db import models

from django.db import models
import datetime

class Post(models.Model):
        author = models.CharField(max_length=100)
        title = models.CharField(max_length=150)
        bodytext = models.TextField()
        pub_date = models.DateTimeField()
        tag = models.ManyToManyField('Tag')

        def __str__(self):
                return self.title

class Tag(models.Model):
        tag = models.CharField(max_length=100)

        def __str__(self):
                return self.tag
