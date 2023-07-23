from django import forms

from apps.MyPlant.models import ProfileModel, PlantModel


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = ProfileModel

        fields = ["username", "first_name", "last_name"]

        username = forms.CharField(label="Username")
        first_name = forms.CharField(label="First name")
        last_name = forms.CharField(label="Last Name")

class ExtendedProfileForm(ProfileCreationForm):
    image_url = forms.URLField(label="Image URL")


class PlantCreationForm(forms.ModelForm):
    class Meta:
        model = PlantModel

        fields = ["plant_type", "name" ,"image_url", "description", "price"]

        PLANT_TYPES = (
            ("Outdoor Plants", "Outdoor Plants"),
            ("Indoor Plants", "Indoor Plants"),
        )
        plant_type = forms.ChoiceField(label="Type:", choices=PLANT_TYPES)
        name = forms.CharField(label="Name:")
        image_url = forms.URLField(label="Image URL:")
        description = forms.CharField(label="Description:", widget=forms.Textarea)
        price = forms.FloatField(label="Price:")

