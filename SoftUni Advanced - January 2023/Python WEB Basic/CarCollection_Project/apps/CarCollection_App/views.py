from django.shortcuts import render, redirect

from apps.CarCollection_App.forms import *
from apps.CarCollection_App.models import *


# Create your views here.

#User
#====================================================================================================
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
    return render(request, "index.html", context)



def catalogue(request):
    context = get_profile()

    cars = CarModel.objects.all()
    context.update({"cars": cars})

    return render(request, "catalogue.html", context)


#profile
#====================================================================================================




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

    return render(request, "profile-create.html", context)



def profile_details(request):
    pass



def profile_edit(request):
    pass



def profile_delete(request):
    pass


#Car
#====================================================================================================

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



def car_details(request, pk):
    context = get_profile()

    car = CarModel.objects.filter(pk=pk).get()
    context.update({"car": car})

    return render(request, "car-details.html", context)



def car_edit(request, pk):
    context = get_profile()

    car = CarModel.objects.filter(pk=pk).get()

    if request.method == "POST":
        form = CarCreationForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    else:
        form = CarCreationForm(instance=car)

    context.update({"form": form})

    return render(request, "car-edit.html", context)



def car_delete(request, pk):
    context = get_profile()

    car = CarModel.objects.get(pk=pk)

    if request.method == "POST":
        car.delete()
        return redirect("catalogue")

    context.update({"car": car})

    return render(request, "car-delete.html", context)


