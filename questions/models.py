from django.db import models
from landing_page.models import Pengguna

# Reference from Codemy.com and geeksforgeeks.org
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

class Post(models.Model):
    user = models.ForeignKey(
        Pengguna,
        models.SET_NULL,
        blank=True,
        null=True
    )
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name="comment"
    )
    user = models.ForeignKey(
        Pengguna,
        models.SET_NULL,
        blank=True,
        null=True
    )
    body = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return "%s's Comment on %s" % (self.user.username, self.post.title)