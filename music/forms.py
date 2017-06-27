from django import forms
from django.contrib.auth.models import User
from .models import Oglas, Employee
from datetime import datetime

class OglasForm(forms.ModelForm):

    class Meta:
        model = Oglas
        fields = ['ime_oglasa', 'slike', 'opis', 'cena', 'grad', 'kategorija', 'slug', 'stanje']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['broj', 'lokacija']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['broj', 'lokacija']

    def save(self, user=None):
        user_profile = super(UserProfileForm, self).save(commit=False)
        emp = Employee.objects.get(user=user)
        if user:
            user_profile.user = user
        user_profile.save()
        emp.save()
        return user_profile

class EditForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['broj', 'lokacija']