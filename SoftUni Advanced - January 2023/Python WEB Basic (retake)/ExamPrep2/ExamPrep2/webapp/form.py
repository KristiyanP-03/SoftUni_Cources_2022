from django import forms

from ExamPrep2.webapp.models import Profile


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
