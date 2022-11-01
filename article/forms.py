from dataclasses import field
from article.models import Article, Comment
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class article_form(forms.ModelForm):
    class Meta:
        model = Article
        fields =('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'masukkan judul'}),
            'body': forms.TextInput(attrs={'class':'form-control', 'placeholder':'masukkan artikel'}),
            
        }

class comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('body',)

        widgets ={
            'body': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tulis komentar'}),
        }