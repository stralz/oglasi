from django import forms
from django.contrib.auth.models import User

from .models import Oglas


class OglasForm(forms.ModelForm):

    class Meta:
        model = Oglas
        fields = ['ime_oglasa', 'slike', 'opis', 'kategorije', 'slug']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
