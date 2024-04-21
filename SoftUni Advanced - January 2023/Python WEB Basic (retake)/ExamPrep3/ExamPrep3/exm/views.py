from django.shortcuts import render, redirect

from ExamPrep3.exm.forms import *
from ExamPrep3.exm.models import *


# Create your views here.
def get_profile():
    profile = None
    context = {}

    try:
        profile = Profile.objects.get()

    except Profile.DoesNotExist:
        profile = None
    if profile is None:
        context = {"profile_exist": False}
    else:
        context = {"profile_exist": True}

    return context


def index(request):
    context = get_profile()
    return render(request, 'index.html', context)


def catalogue(request):
    pass


def car_create(request):
    context = get_profile()

    if request.method == "POST":
        form = CarCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    else:
        form = CarCreationForm()

    context.update({"form": form})

    return render(request, "car-create.html", context)


def car_id_details(request, id):
    pass


def car_id_edit(request, id):
    pass


def car_id_delete(request, id):
    pass


def profile_create(request):
    context = get_profile()
    if context == {"profile_exist": True}:
        return redirect("index")

    if request.method == "GET":
        form = ProfileCreationForm()
    else:
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {"profile_creation_form": form}

    return render(request, "profile-create.html", context)


def profile_details(request):
    context = get_profile()

    profile = Profile.objects.get()

    context.update({"profile": profile})

    return render(request, "profile-details.html", context)


def profile_edit(request):
    profile = Profile.objects.get()

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            profile.save()
            return redirect('profile_details')
    else:
        form = ProfileEditForm(instance=profile)

    context = {'form': form}
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    context = get_profile()

    profile = Profile.objects.get()

    if request.method == "POST":
        profile.delete()
        return redirect("index")

    context.update({"profile": profile})
    return render(request, "profile-delete.html", context)
