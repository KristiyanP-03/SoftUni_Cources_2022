from django import forms

from exam_app.models import *


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = ProfileModel

        fields = ["email", "profile_picture", "password"]

        email = forms.CharField(label="EMAIL")
        profile_picture = forms.CharField(label="PROFILE PICTURE")
        password = forms.CharField(label="PASSWORD", widget=forms.PasswordInput)


class EventCreationForm(forms.ModelForm):
    EVENT_CATEGORIES = [
        ('Sports', 'Sports'),
        ('Festivals', 'Festivals'),
        ('Conferences', 'Conferences'),
        ('Performing Art', 'Performing Art'),
        ('Concerts', 'Concerts'),
        ('Theme Party', 'Theme Party'),
        ('Other', 'Other'),
    ]

    category = forms.ChoiceField(label="Category:", choices=EventModel.EVENT_CATEGORIES)
    event_name = forms.CharField(label="Event Name:")
    event_image = forms.URLField(label="Image URL:")
    description = forms.CharField(label="Description:", widget=forms.Textarea)
    date = forms.DateTimeField()
    class Meta:
        model = EventModel

        fields = ["event_name" ,"category", "description", "date", "event_image"]


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ["first_name", "last_name", "email", "profile_picture", "password"]

    first_name = forms.CharField(label="First Name:")
    last_name = forms.CharField(label="Last Name:")
    email = forms.EmailField(label="Email:")
    profile_picture = forms.CharField(label="Profile Picture:")
    password = forms.CharField(label="Password:", widget=forms.PasswordInput)







class EventDeleteForm(forms.ModelForm):
    EVENT_CATEGORIES = [
        ('Sports', 'Sports'),
        ('Festivals', 'Festivals'),
        ('Conferences', 'Conferences'),
        ('Performing Art', 'Performing Art'),
        ('Concerts', 'Concerts'),
        ('Theme Party', 'Theme Party'),
        ('Other', 'Other'),
    ]

    category = forms.ChoiceField(label="Category:", choices=EventModel.EVENT_CATEGORIES, disabled=True)
    event_name = forms.CharField(label="Event Name:", disabled=True)
    event_image = forms.URLField(label="Image URL:", disabled=True)
    description = forms.CharField(label="Description:", widget=forms.Textarea, disabled=True)
    date = forms.DateTimeField(disabled=True)

    class Meta:
        model = EventModel
        fields = ["event_name", "category", "description", "date", "event_image"]