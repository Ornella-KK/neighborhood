from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'neighborhood']


class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['user']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['neighborhood']

class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        exclude = ['posted_by', 'neighborhood', 'date_posted']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'alert', 'date_posted']
