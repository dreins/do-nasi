from django import forms

class create_form(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget= forms.Textarea)