from django import forms

from app.models import *


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["nickname", "first_name", "last_name", "chef"]
        labels = {
            "nickname": "Nickname",
            "first_name": "First Name",
            "last_name": "Last Name",
            "chef": "Chef",
        }


class ExtendedProfileForm(ProfileCreationForm):
    bio = forms.CharField(
        label="Bio",
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}),
        required=False
    )

    class Meta(ProfileCreationForm.Meta):
        fields = ProfileCreationForm.Meta.fields + ["bio"]


class RecipeCreationForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "cuisine_type", "ingredients", "instructions", "cooking_time", "image_url"]
        labels = {
            "title": "Title",
            "cuisine_type": "Cuisine Type",
            "ingredients": "Ingredients",
            "instructions": "Instructions",
            "cooking_time": "Cooking Time",
            "image_url": "Image URL",
        }
        help_texts = {
            "ingredients": "Ingredients must be separated by a comma and space.",
            "cooking_time": "Provide the cooking time in minutes.",
        }
        widgets = {
            "ingredients": forms.TextInput(
                attrs={'placeholder': 'ingredient1, ingredient2, ...'}
            ),
            "instructions": forms.Textarea(
                attrs={'placeholder': 'Enter detailed instructions here...'}
            ),
            "image_url": forms.TextInput(
                attrs={'placeholder': 'Optional image URL here...'}
            ),
        }

