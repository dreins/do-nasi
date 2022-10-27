from __future__ import with_statement
from typing import Text
from django import forms
from .models import *

class create_form(forms.Form):
	title = forms.CharField(widget=forms.TextInput)
	description = forms.CharField(widget= forms.TextInput)
	deadline = forms.CharField(widget= forms.TextInput)
    