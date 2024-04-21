from django import forms

from ExamPrep3.exm.models import *


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
            'password': 'Password'
        }
        help_texts = {
            'age': 'Age requirement: 21 years and above.'
        }
        widgets = {
            'password': forms.PasswordInput()
        }


class ProfileEditForm(ProfileCreationForm):
    first_name = forms.CharField(label='First Name', required=False)
    last_name = forms.CharField(label='Last Name', required=False)
    profile_picture = forms.URLField(label='Profile Picture', required=False)


class CarCreationForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']
        labels = {
            'type': 'Type',
            'model': 'Model',
            'year': 'Year',
            'image_url': 'Image URL',
            'price': 'Price'
        }


class CarEditForm(CarCreationForm):
    pass
