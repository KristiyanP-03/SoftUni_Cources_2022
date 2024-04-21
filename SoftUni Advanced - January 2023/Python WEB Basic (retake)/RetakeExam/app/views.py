from django.shortcuts import render, redirect

from app.forms import *
from app.models import *


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
    return render(request, "home-page.html", context)


def catalogue(request):
    context = get_profile()

    recipes = Recipe.objects.all()
    context.update({"recipes": recipes})

    return render(request, "catalogue.html", context)


def recipe_create(request):
    context = get_profile()

    if request.method == "POST":
        form = RecipeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    else:
        form = RecipeCreationForm()

    context.update({"form": form})

    return render(request, "create-recipe.html", context)


def recipe_details(request, pk):
    context = get_profile()
    recipe = Recipe.objects.get(pk=pk)
    ingredients_list = recipe.ingredients.split(",")
    context.update({
        'recipe': recipe, 'ingredients_list': ingredients_list
    })

    return render(request, 'details-recipe.html', context)


def recipe_edit(request, pk):
    context = get_profile()

    recipe = Recipe.objects.filter(pk=pk).get()

    if request.method == "POST":
        form = RecipeCreationForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    else:
        form = RecipeCreationForm(instance=recipe)

    context.update({"form": form})

    return render(request, "edit-recipe.html", context)


def recipe_delete(request, pk):
    context = get_profile()

    recipe = Recipe.objects.get(pk=pk)

    if request.method == "POST":
        recipe.delete()
        return redirect("catalogue")
    else:
        form = RecipeCreationForm(instance=recipe)
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True

    context.update({"form": form})
    return render(request, 'delete-recipe.html', context)


def profile_create(request):
    context = get_profile()
    if context == {"profile_exist": True}:
        return redirect("catalogue")

    if request.method == "GET":
        form = ProfileCreationForm()
    else:
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue")

    context = {"profile_creation_form": form}

    return render(request, "create-profile.html", context)


def profile_details(request):
    context = get_profile()

    profile = Profile.objects.get()
    count_of_recipes = Recipe.objects.count()

    context.update({"profile": profile, "recipes_count": count_of_recipes})

    return render(request, "details-profile.html", context)


def profile_edit(request):
    profile = Profile.objects.get()

    if request.method == 'POST':
        form = ExtendedProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            profile.save()
            return redirect('details_profile')
    else:
        form = ExtendedProfileForm(instance=profile)

    context = get_profile()
    context['form'] = form
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    context = get_profile()

    profile = Profile.objects.get()

    if request.method == "POST":
        Recipe.objects.all().delete()
        profile.delete()
        return redirect("index")

    context.update({"profile": profile})
    return render(request, "delete-profile.html", context)

