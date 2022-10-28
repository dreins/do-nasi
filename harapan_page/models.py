import email
from django.db import models
from landing_page.models import Pengguna

class HarapanDonatur(models.Model):
    user = models.ForeignKey(
        Pengguna,
        on_delete=models.CASCADE,
        null = True,
        blank = True
    )
    username = models.CharField(max_length=50, blank = True)
    email = models.CharField(max_length=50, blank = True)
    created_at = models.DateField(auto_now=True)
    text = models.TextField()