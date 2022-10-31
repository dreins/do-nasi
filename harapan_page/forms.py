from django.forms import ModelForm
from harapan_page.models import HarapanDonatur

class HarapanForm(ModelForm):
    class Meta:
        model = HarapanDonatur
        fields = ['text']