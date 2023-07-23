from django.shortcuts import render

from apps.functionality.get_profile import get_profile
from apps.functionality.view_forms import view_form
from apps.user_profile.forms import ProfileModelBaseForm
from apps.user_profile.models import ProfileModel

# Create your views here.
def home_page(request):
    profile = get_profile(ProfileModel)

    if profile:
        return view_form(request=request, base_form=ProfileModelBaseForm, redirect_url='home_page',
                         base_url="common/home-page.html")

    return view_form(request=request, base_form=ProfileModelBaseForm, redirect_url='home_page',
                     base_url="common/home-page.html", additional_data={"no_profile": True})

def dashboard(request):
    pass
