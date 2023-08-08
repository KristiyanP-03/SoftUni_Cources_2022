from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth import logout, login, authenticate, get_user_model

from apps.FoodieHaven_app.forms import *
from apps.FoodieHaven_app.models import *


# Create your views here.
#--------------------------------------------------------------------------------------------------
#==================================================================================================
#Main view
def index(request):
    return render(request, "index.html")



#Public view
def recipes(request):
    pass




#Profile views
#==================================================================================================
class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'profile-register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)

        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)

        return response
class LoginView(LoginView):
    template_name = 'profile-log-in.html'
    redirect_authenticated_user = True

class LogoutView(LogoutView):
    next_page = reverse_lazy('index')

class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'profile-details.html'
    context_object_name = 'profile'
    model = ProfileModel

    def get_object(self, queryset=None):
        return self.request.user


class EditProfileView(LoginRequiredMixin, UpdateView):
    form_class = ProfileEditForm
    template_name = 'profile-edit.html'
    success_url = reverse_lazy('profile details')

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile details')

class DeleteProfileView(LoginRequiredMixin, DeleteView):
    model = ProfileModel
    template_name = 'profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('index')





#Recepies view
#==================================================================================================
def user_recipes(request):
    recipes = RecipeModel.objects.all()
    return render(request, 'user-recipes.html', {'recipes': recipes})

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('user recipes')
    else:
        form = RecipeForm()

    return render(request, 'recipe-create.html', {'form': form})

def recipe_details(request):
    pass

def recipe_edit(request):
    pass

def recipe_delete(request):
    pass
