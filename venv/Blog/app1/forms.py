from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# use this form to add new post and using the widgets
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'description')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control',"placeholder":"Readonly Title here..."}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'})
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
        fields = ('username', 'email','password1','password2')