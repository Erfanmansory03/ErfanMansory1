from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.


class signupForm(forms.Form):
    name=forms.CharField(label='name',max_length=20)
    username=forms.CharField(label='username',max_length=20)
    password=forms.CharField(label='password',max_length=20)
