from email.policy import default
from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

class HarapanDonatur(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null = True,
        blank = True
    )
    created_at = models.DateField(auto_now=True)
    text = models.TextField()
    harapan_image = models.ImageField(upload_to='harapan_image', default=None)
    likes = models.IntegerField(default=0)