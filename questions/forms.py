from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {
            'body': forms.Textarea()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body')
        widgets = {
            'body': forms.Textarea()
        }