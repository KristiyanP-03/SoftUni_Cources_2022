from django.core.validators import *
from django.db import models

# Error validating functions
def first_letter_must_be_alpha(input):
    if not input[0].isalpha():
        raise ValidationError("Your name must start with a letter!")

def use_leters_only(input):
    for char in input:
        if not char.isalpha():
            raise ValidationError("Fruit name should contain only letters!")

# Create your models here.
class ProfileModel(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=25,
                                  validators=[MinLengthValidator(2), first_letter_must_be_alpha])
    last_name = models.CharField(verbose_name="Last Name", max_length=35,
                                  validators=[MinLengthValidator(1), first_letter_must_be_alpha])
    email = models.EmailField(verbose_name="Email", max_length=40,)
    password = models.CharField(verbose_name="Password", max_length=20,
                                validators=[MinLengthValidator(8),])
    image_url = models.URLField(verbose_name="Image URL", blank=True, null=True)
    age = models.IntegerField(verbose_name="Age", default=18, blank=True)

class FruitModel(models.Model):
    name = models.CharField(verbose_name="Name", max_length=30,
                                  validators=[MinLengthValidator(2), use_leters_only])
    image_url = models.URLField(verbose_name="Image URL")
    description = models.TextField(verbose_name="Description")
    nutrition = models.TextField(verbose_name="Nutrition")


