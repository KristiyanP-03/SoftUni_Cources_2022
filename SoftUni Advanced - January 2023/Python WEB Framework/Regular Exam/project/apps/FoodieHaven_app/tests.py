from django.test import TestCase
from django.urls import reverse

from apps.FoodieHaven_app.forms import *
from apps.FoodieHaven_app.models import *
from .views import *



# Create your tests here.


class ProfileModelTestCase(TestCase):
    def test_profile_model_creation(self):
        profile = ProfileModel.objects.create(username="testuser", email="test@example.com")
        self.assertEqual(profile.username, "testuser")
        self.assertEqual(profile.email, "test@example.com")
        self.assertEqual(str(profile), "testuser")





class RegistrationFormTestCase(TestCase):
    def test_registration_form_valid(self):
        form_data = {
            "username": "testuser",
            "password": "testpassword",
            "repeat_password": "testpassword",
            "email": "test@example.com",
            "agree_privacy": True,
            "agree_show_profile": True,
            "agree_rules": True,
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid(self):
        form_data = {
            "username": "testuser",
            "password": "testpassword",
            "repeat_password": "wrongpassword",
            "email": "invalidemail",
            "agree_privacy": False,
            "agree_show_profile": True,
            "agree_rules": True,
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())







class RecipeFormTestCase(TestCase):
    def test_recipe_form_valid(self):
        user = ProfileModel.objects.create(username="chef", email="chef@example.com")
        form_data = {
            "title": "Test Recipe",
            "time_category": "breakfast",
            "type_category": "appetizer",
            "description": "This is a test recipe.",
            "ingredients": "Ingredient 1, Ingredient 2",
            "instructions": "Step 1, Step 2",
            "time_to_cook": "15",
        }
        form = RecipeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_recipe_form_invalid(self):
        user = ProfileModel.objects.create(username="chef", email="chef@example.com")
        form_data = {
            "title": "",
            "time_category": "breakfast",
            "type_category": "appetizer",
            "description": "This is a test recipe.",
            "ingredients": "",
            "instructions": "",
            "time_to_cook": "15",
        }
        form = RecipeForm(data=form_data)
        self.assertFalse(form.is_valid())






class RegisterViewTestCase(TestCase):
    def test_register_view_redirect_authenticated_user(self):
        user = ProfileModel.objects.create(username="testuser", email="test@example.com")
        self.client.force_login(user)
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))

    def test_register_view_valid_form(self):
        form_data = {
            "username": "newuser",
            "password": "newpassword",
            "repeat_password": "newpassword",
            "email": "newuser@example.com",
            "agree_privacy": True,
            "agree_show_profile": True,
            "agree_rules": True,
        }
        response = self.client.post(reverse("register"), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))







class ReportUserViewTestCase(TestCase):
    def test_report_user_view_valid_form(self):
        reporter = ProfileModel.objects.create(username="reporter", email="reporter@example.com")
        reported_user = ProfileModel.objects.create(username="reported", email="reported@example.com")
        self.client.force_login(reporter)
        form_data = {
            "description": "This is a test report.",
        }
        response = self.client.post(reverse("report_user", args=[reported_user.pk]), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))









class ProfileModelTestCase(TestCase):
    def test_profile_model_str(self):
        profile = ProfileModel(username="testuser", email="test@example.com")
        self.assertEqual(str(profile), "testuser")

    def test_profile_model_username_length_validator(self):
        with self.assertRaises(ValidationError):
            ProfileModel(username="u", email="test@example.com").full_clean()






class RecipeModelTestCase(TestCase):
    def setUp(self):
        self.user = ProfileModel.objects.create_user(username="testuser", password="testpassword")

    def test_recipe_model_creation(self):
        recipe = RecipeModel.objects.create(
            title="Test Recipe",
            chef=self.user,
            time_category="breakfast",
            type_category="main_course",
            description="Test recipe description",
            ingredients="Ingredient 1, Ingredient 2",
            instructions="Step 1, Step 2",
            time_to_cook="30"
        )
        self.assertEqual(recipe.title, "Test Recipe")
        self.assertEqual(recipe.chef, self.user)
        self.assertEqual(recipe.time_category, "breakfast")
        self.assertEqual(recipe.type_category, "main_course")