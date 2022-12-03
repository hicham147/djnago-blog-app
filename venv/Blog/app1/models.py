from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return self.post +'|'+ str(self.author)
    
    def get_absolute_url(self):
        return reverse('index',args=self.id)