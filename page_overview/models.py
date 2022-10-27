from audioop import reverse
from email.policy import default
from django.db import models
from landing_page.models import Pengguna
from django.urls import reverse

# Create your models here.
class Donasi(models.Model):
    user = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    title = models.TextField()
    deadline = models.DateField(auto_now_add = False, auto_now = False, blank = True, null = True)
    description =  models.TextField()
    Donation = models.BooleanField(default = False)
    
