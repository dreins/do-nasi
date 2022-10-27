from django import forms
from .models import Pengguna
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class FormRegister(UserCreationForm):
    class Meta: 
        model = Pengguna
        fields = ('name', 'email', 'username', 'password1', 'password2', 'role')


    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Pengguna.objects.exclude(pk=self.instance.pk).get(email=email)
        except Pengguna.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % email)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = Pengguna.objects.exclude(pk=self.instance.pk).get(username=username)
        except Pengguna.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)

class FormLogin(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    class Meta: 
        model = Pengguna
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login. Please, try again.")

    # check if username or email is already exist
    # referensi: https://www.folkstalk.com/2022/09/check-if-username-exists-in-database-django-with-code-examples.html#
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if Pengguna.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
    #         raise forms.ValidationError('Username is already used.')
    #     return username

    # def clean_email(self):
    #     email = self.cleaned_data['email'].lower
    #     if Pengguna.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
    #         raise forms.ValidationError('Email is already used.')
    #     return email
    