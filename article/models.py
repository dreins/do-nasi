from django.db import models
from django.contrib.auth.models import User
from landing_page.models import Pengguna
from ckeditor.fields import RichTextField
from django.utils.text import slugify 


class Article(models.Model):
    user = models.ForeignKey(Pengguna,on_delete =models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=250, unique=True)
    body = models.TextField(blank=True)
    slug = models.SlugField(blank=True, null=True)



class Comment(models.Model):
    post = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(Pengguna,on_delete =models.CASCADE)
    body = models.TextField()
    date_added =models.DateTimeField(auto_now_add=True)

    def __str___(self):
        return '%s - %s' %(self.post.title, self.name)
# Create your models here.
