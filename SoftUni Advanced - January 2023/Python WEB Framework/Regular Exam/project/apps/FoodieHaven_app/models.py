from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


# Profile Model
# #=====================================================================================================================
class ProfileModel(AbstractUser):
    profile_picture = models.URLField(verbose_name="Profile Picture (URL)", blank=True, null=True)
    bio = models.TextField(verbose_name="Bio", blank=True, null=True)

    def __str__(self):
        return self.username



# Recepie Model
#=====================================================================================================================
def validate_unique_title(input):
    if RecipeModel.objects.filter(title=input).exists():
        raise ValidationError("A recipe with this title already exists.")
def cant_be_empty_string(input):
    if not input.strip():
        raise ValidationError("Must have any ingredient listed")


class RecipeModel(models.Model):
    TIME_CATEGORY_CHOICES = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    )
    TYPE_CATEGORY_CHOICES = (
        ('appetizer', 'Appetizer'),
        ('main_course', 'Main Course'),
        ('dessert', 'Dessert'),
        ('beverage', 'Beverage'),
    )
    TIME_TO_COOK_CHOICES = (
        ('15', '15 minutes'),
        ('30', '30 minutes'),
        ('45', '45 minutes'),
        ('60', '1 hour'),
        ('90', '1 hour 30 minutes'),
        ('120', '2 hours or more'),
    )

    title = models.CharField(max_length=200, validators=[validate_unique_title], verbose_name="Recipe Title")
    picture = models.URLField(verbose_name="Picture (URL)", blank=True, null=True)
    chef = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Chef")
    time_category = models.CharField(max_length=20, choices=TIME_CATEGORY_CHOICES, verbose_name="Time Category")
    type_category = models.CharField(max_length=20, choices=TYPE_CATEGORY_CHOICES, verbose_name="Type Category")
    description = models.TextField(verbose_name="Description")
    ingredients = models.TextField(validators=[cant_be_empty_string], verbose_name="Ingredients")
    instructions = models.TextField(verbose_name="Instructions")
    time_to_cook = models.CharField(max_length=3, choices=TIME_TO_COOK_CHOICES, verbose_name="Time to Cook")

    def __str__(self):
        return self.title