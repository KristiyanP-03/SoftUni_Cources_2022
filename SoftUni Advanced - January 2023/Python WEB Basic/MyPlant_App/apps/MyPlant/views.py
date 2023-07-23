from django.shortcuts import render, redirect

from apps.MyPlant.forms import *
from apps.MyPlant.models import ProfileModel


def get_profile():
    profile = None
    context = {}

    try:
        profile = ProfileModel.objects.get()

    except ProfileModel.DoesNotExist:
        profile = None
    if profile is None:
        context = { "profile_exist": False }
    else:
        context = {"profile_exist": True}

    return context


# Create your views here.
def index(request):
    context = get_profile()
    return render(request, "home-page.html", context)


def profile_create(request):
    context = get_profile()
    if context == { "profile_exist": True }:
        return redirect("index")

    if request.method == "GET":
        form = ProfileCreationForm()
    else:
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {"profile_creation_form": form}

    return render(request, "create-profile.html", context)


def catalogue(request):
    context = get_profile()

    plants = PlantModel.objects.all()
    context.update({"plants": plants})

    return render(request, "catalogue.html", context)


def plant_create(request):
    context = get_profile()

    if request.method == "POST":
        form = PlantCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    else:
        form = PlantCreationForm()


    context.update({"form": form})

    return render(request, "create-plant.html", context)


def plant_details(request, pk):
    context = get_profile()

    plant = PlantModel.objects.filter(pk=pk).get()
    context.update({"plant": plant})

    return render(request, "plant-details.html", context)


def plant_edit(request, pk):
    context = get_profile()

    plant = PlantModel.objects.filter(pk=pk).get()

    if request.method == "POST":
        form = PlantCreationForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    else:
        form = PlantCreationForm(instance=plant)


    context.update({"form": form})

    return render(request, "edit-plant.html", context)


def plant_delete(request, pk):
    context = get_profile()

    plant = PlantModel.objects.get(pk=pk)

    if request.method == "POST":
        plant.delete()
        return redirect("catalogue")

    context.update({"plant": plant})

    return render(request, "delete-plant.html", context)


def profile_details(request):
    context = get_profile()

    profile = ProfileModel.objects.get()
    count_of_plants = PlantModel.objects.count()

    context.update({"profile":profile, "plants_count":count_of_plants})

    return render(request, "profile-details.html", context)


def profile_edit(request):
    profile = ProfileModel.objects.get()

    if request.method == 'POST':
        form = ExtendedProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile.profile_picture = form.cleaned_data['image_url']
            form.save()
            profile.save()
            return redirect('profile details')
    else:
        form = ExtendedProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    context = get_profile()

    profile = ProfileModel.objects.get()

    if request.method == "POST":
        profile.delete()
        return redirect("index")

    context.update({"profile": profile})
    return render(request, "delete-profile.html", context)