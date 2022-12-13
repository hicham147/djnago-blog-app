from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField



class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    description = RichTextField(blank=True,null=True)
    date_posted = models.DateField(auto_now_add=True)
    like = models.ManyToManyField(User,related_name="post_like")
    def __str__(self):
        return self.title +'|'+ str(self.author)
    
    def get_absolute_url(self):
        return reverse('index',args=self.id)
    
    # returne the count of the likes
    def like_count(self):
        return self.like_count.count()