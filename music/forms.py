from django import forms
from django.contrib.auth.models import User

from .models import Oglas


class OglasForm(forms.ModelForm):

    class Meta:
        model = Oglas
        fields = ['vlasnik', 'ime_oglasa', 'slike']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
