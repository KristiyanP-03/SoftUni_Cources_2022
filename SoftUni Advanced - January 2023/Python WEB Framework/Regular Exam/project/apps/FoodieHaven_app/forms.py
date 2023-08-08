from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import ProfileModel, RecipeModel


# Profile Forms
#=====================================================================================================
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    repeat_password = forms.CharField(widget=forms.PasswordInput(), label="Repeat Password")
    agree_privacy = forms.BooleanField(label="I agree with the privacy policy")
    agree_show_profile = forms.BooleanField(label="I agree for my profile to be shown")
    agree_rules = forms.BooleanField(label="I agree to the site rules")

    class Meta:
        model = ProfileModel
        fields = [
            'password', 'repeat_password', 'username', 'email', 'agree_privacy', 'agree_show_profile', 'agree_rules'
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')

        if password and repeat_password and password != repeat_password:
            raise ValidationError("Passwords do not match. Please try again.")

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.password = make_password(self.cleaned_data['password'])
        if commit:
            instance.save()
        return instance

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'email', 'profile_picture', 'bio']


# Recepie Forms
#=====================================================================================================
class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = [
            'title',
            'picture',
            'time_category',
            'type_category',
            'description',
            'ingredients',
            'instructions',
            'time_to_cook',
        ]

    def save(self, user, *args, **kwargs):
        instance = super(RecipeForm, self).save(commit=False)
        instance.chef = user
        instance.save()
        return instance