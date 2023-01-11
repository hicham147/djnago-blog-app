from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField()
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
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True, null=True)
    image  = models.ImageField(default="default.jpg", upload_to="profile_pics")
    
    def __str__(self):
        return f"{self.user} Profile"
    
def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
        

post_save.connect(create_profile,sender=User)


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    content = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.post.title} comments'