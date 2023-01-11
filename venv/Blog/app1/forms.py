from django import forms
from .models import Post,Profile,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# use this form to add new post and using the widgets
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'description',)
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control',"placeholder":"Readonly Title here..."}),
            'author':forms.Select(attrs={'class':'form-control'}),
            
            'description':forms.Textarea(attrs={'class':'form-control'})
        }
    
        
class PostimageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image',)
        widgets = {
            'image':forms.ImageField(),
        }

# use this form to update the post and using the widgets
class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control',"placeholder":"Readonly Title here..."}),
            'description':forms.Textarea(attrs={'class':'form-control'})
        }
        
        
        
        
class UserFormCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control',"type":"text"}),
            'email':forms.EmailInput(attrs={'class':'form-control',"type":"email"})
        }
        
class ProfileFormUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
        widgets = {
            'user':forms.ImageField(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content':forms.TextInput(attrs={'class':'form-control',"type":"text"}),
        }
