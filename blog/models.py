from django.db import models
from django.utils import timezone


# Models for the database of the pieces users can request
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='media/img')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
	
    def __str__(self):
        return 'Title: ' + str(self.title) + '. Created on: ' + str(self.created_date) + '. Published on: ' + str(self.published_date)
