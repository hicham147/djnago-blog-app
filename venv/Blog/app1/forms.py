from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'description')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control',"placeholder":"Readonly Title here..."}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'})
        }