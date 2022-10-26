from email.policy import default
from django.db import models
from django.conf import settings

class HarapanDonatur(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null = True,
        blank = True
    )
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    harapan_image = models.ImageField(upload_to='harapan_image', default=None)