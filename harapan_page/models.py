from django.contrib.auth import get_user_model
from django.db import models

class HarapanDonatur(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null = True,
        blank = True
    )
    created_at = models.DateField(auto_now=True)
    text = models.TextField()
    likes = models.IntegerField(default=0)