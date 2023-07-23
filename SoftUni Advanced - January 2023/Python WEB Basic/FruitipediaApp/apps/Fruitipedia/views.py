from django.shortcuts import render, redirect

from apps.Fruitipedia.forms import ProfileCreationForm, FruitCreationForm, ProfileEditForm
from apps.Fruitipedia.models import ProfileModel, FruitModel


# Create your views here.

def get_profile():
    profile = None
    context = {}

    try:
        profile = ProfileModel.objects.get()
    except ProfileModel.DoesNotExist:
        profile = None

    if profile is None:
        context = {
            "profile_exist": False,
        }
    else:
        context = {
            "profile_exist": True,
        }

    return context


def index(request):
    context = get_profile()

    return render(request, "index.html", context)


def dashboard(request):
    context = get_profile()

    fruits = FruitModel.objects.all()
    context.update({'fruits': fruits})

    return render(request, "dashboard.html", context)


def create(request):
    context = get_profile()


    fruit_form = FruitCreationForm(request.POST)
    if fruit_form.is_valid():
        fruit_form.save()
        return redirect('dashboard')
    context.update({'fruit_form': fruit_form})

    return render(request, "create-fruit.html", context)


def pk_details(request, pk):
    context = get_profile()

    fruit = FruitModel.objects.filter(pk=pk).get()
    context.update({'fruit': fruit})

    return render(request, "details-fruit.html", context)


def pk_edit(request, pk):
    context = get_profile()

    fruit = FruitModel.objects.get(pk=pk)

    if request.method == "POST":
        form = FruitCreationForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FruitCreationForm(instance=fruit)

    context.update({'edit_fruit_form': form})
    return render(request, "edit-fruit.html", context)


def pk_delete(request, pk):
    context = get_profile()

    fruit = FruitModel.objects.get(pk=pk)

    if request.method == "POST":
        form = FruitCreationForm(request.POST, instance=fruit)
        if form.is_valid():
            fruit.delete()
            return redirect('dashboard')
    else:
        form = FruitCreationForm(instance=fruit)

    context.update({'delete_fruit_form': form})
    return render(request, "delete-fruit.html", context)


def profile_create(request):
    if get_profile() == {"profile_exist": True,}:
        return redirect('index')

    if request.method == "GET":
        profile_form = ProfileCreationForm()
    else:
        profile_form = ProfileCreationForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')

    context = { 'profile_form': profile_form, }
    return render(request, "create-profile.html", context)


def profile_details(request):
    context = get_profile()

    profile = ProfileModel.objects.get()
    posts_count = FruitModel.objects.count()
    context.update({"profile":profile, "posts": posts_count})
    return render(request, "details-profile.html", context)


def profile_edit(request):
    context = get_profile()
    profile = ProfileModel.objects.get()

    if request.method == "POST":
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            # Process and save the form data here
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name = form.cleaned_data['last_name']
            profile.image_url = form.cleaned_data['image_url']
            profile.age = form.cleaned_data['age']
            profile.save()
            return redirect('profile details')
    else:
        # Populate the form with existing profile data
        form = ProfileEditForm(initial={
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'image_url': profile.image_url,
            'age': profile.age,
        })

    context.update({'edit_profile_form': form})
    return render(request, "edit-profile.html", context)


def profile_delete(request):
    context = get_profile()

    profile = ProfileModel.objects.get()

    if request.method == "POST":
        profile.delete()
        return redirect('index')

    context.update({'delete_profile_form': ''})
    return render(request, "delete-profile.html", context)