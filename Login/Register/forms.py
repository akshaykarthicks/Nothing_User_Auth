from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.db import models
from django.contrib.auth.models import User
from django import forms
#pip install django-crispy-forms

class registerform(UserCreationForm):
    email=forms.EmailField()


    class Meta:
        model=User
        fields=["username","email","password1","password2"]  #fields to be displayed