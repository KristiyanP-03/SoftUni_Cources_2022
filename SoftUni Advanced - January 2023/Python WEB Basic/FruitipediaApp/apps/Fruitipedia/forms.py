from django import forms
from .models import ProfileModel, FruitModel


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {
            'first_name': False,
            'last_name': False,
            'email': False,
            'password': False,
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }

class FruitCreationForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = ['name', 'image_url', 'description', 'nutrition']
        labels = {
            'name': False,
            'image_url': False,
            'description': False,
            'nutrition': False
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.TextInput(attrs={'placeholder': 'Nutrition Info'})
        }



class ProfileEditForm(forms.Form):
    first_name = forms.CharField(label="First Name:")
    last_name = forms.CharField(label="Last Name:")
    image_url = forms.URLField(label="Image URL:")
    age = forms.IntegerField(label="Age:")