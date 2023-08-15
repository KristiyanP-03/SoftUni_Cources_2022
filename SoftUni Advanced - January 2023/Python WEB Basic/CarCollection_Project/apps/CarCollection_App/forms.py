from django import forms

from apps.CarCollection_App.models import *


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = ProfileModel

        fields = ["username", "email", "age", "password"]

        username = forms.CharField(label="Username:")
        email = forms.CharField(label="Email:")
        age = forms.IntegerField(label="Age:")
        password = forms.CharField(label="Password:")


class CarCreationForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['type', 'model', 'year', 'image_url', 'price']