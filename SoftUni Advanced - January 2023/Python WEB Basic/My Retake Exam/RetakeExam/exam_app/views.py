from django.shortcuts import render, redirect

from exam_app.forms import *
from exam_app.models import *


# Create your views here.
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





def home_page(request):
    context = get_profile()
    return render(request, "shared/home-page.html", context)




def dashboard(request):
    context = get_profile()

    events = EventModel.objects.all()
    context.update({"events": events})

    return render(request, "events/dashboard.html", context)












def event_create(request):
    context = get_profile()

    if request.method == "POST":
        form = EventCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = EventCreationForm()


    context.update({"form": form})

    return render(request, "events/event-create.html", context)


def event_details(request, pk):
    context = get_profile()

    event = EventModel.objects.filter(pk=pk).get()
    context.update({"event": event})

    return render(request, "events/events-details.html", context)


def event_edit(request, pk):
    context = get_profile()

    event = EventModel.objects.filter(pk=pk).get()

    if request.method == "POST":
        form = EventCreationForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = EventCreationForm(instance=event)


    context.update({"form": form})

    return render(request, "events/event-edit.html", context)


def event_delete(request, pk):
    context = get_profile()

    event = EventModel.objects.get(pk=pk)

    form = EventDeleteForm(request.POST, instance=event)


    if request.method == "POST":
        event.delete()
        return redirect("dashboard")

    context.update({"event": event, "form": form})

    return render(request, "events/events-delete.html", context)














def profile_create(request):
    context = get_profile()
    if context == { "profile_exist": True }:
        return redirect("dashboard")

    if request.method == "GET":
        form = ProfileCreationForm()
    else:
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {"profile_creation_form": form}

    return render(request, "profiles/profile-create.html", context)


def profile_details(request):
    context = get_profile()

    profile = ProfileModel.objects.get()
    count_of_events = EventModel.objects.count()

    context.update({"profile":profile, "count_of_events":count_of_events})

    return render(request, "profiles/profile-details.html", context)


def profile_edit(request):
    profile = ProfileModel.objects.get()

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            profile.save()
            return redirect('profile details')
    else:
        form = ProfileEditForm(instance=profile)

    context = {'form': form}
    return render(request, 'profiles/profile-edit.html', context)


def profile_delete(request):
    context = get_profile()

    profile = ProfileModel.objects.get()

    if request.method == "POST":
        events_to_delete = EventModel.objects.all()
        events_to_delete.delete()
        profile.delete()
        return redirect("home page")

    context.update({"profile": profile})
    return render(request, "profiles/profile-delete.html", context)