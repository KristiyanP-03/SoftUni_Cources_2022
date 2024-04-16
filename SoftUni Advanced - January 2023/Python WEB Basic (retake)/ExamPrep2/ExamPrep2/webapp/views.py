from django.shortcuts import render, redirect

from ExamPrep2.webapp.form import ProfileCreationForm
from ExamPrep2.webapp.models import Profile


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
    try:
        profile = Profile.objects.get()
        return render(request, 'home-with-profile.html')
    except Profile.DoesNotExist:
        if request.method == 'POST':
            form = ProfileCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = ProfileCreationForm()
        return render(request, 'home-no-profile.html', {'form': form})


def album_add(request):
    return render(request, 'add-album.html')


def album_details(request, pk):
    return render(request, 'album-details.html')


def album_edit(request, pk):
    return render(request, 'edit-album.html')


def album_delete(request, pk):
    return render(request, 'delete-album.html')


def profile_details(request):
    return render(request, 'profile-details.html')


def profile_delete(request):
    return render(request, 'profile-delete.html')

