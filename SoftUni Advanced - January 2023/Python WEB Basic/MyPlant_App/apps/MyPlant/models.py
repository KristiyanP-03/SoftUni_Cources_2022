from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

def first_letter_must_be_capital(input):
    if not input[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")

def only_leters(input):
    for letter in input:
        if not letter.isalpha():
            raise ValidationError("Plant name should contain only letters!")
            break


# Create your models here.
class ProfileModel(models.Model):
    username = models.CharField(verbose_name="Username", max_length=10, validators=[MinLengthValidator(2)])
    first_name = models.CharField(verbose_name="First Name", max_length=20, validators=[first_letter_must_be_capital])
    last_name = models.CharField(verbose_name="Last Name", max_length=20, validators=[first_letter_must_be_capital])
    profile_picture = models.URLField(verbose_name="Profile Picture", blank=True, null=True)

class PlantModel(models.Model):
    PLANT_TYPES = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants"),
    )
    plant_type = models.CharField(max_length=14, choices=PLANT_TYPES)
    name = models.CharField(verbose_name="Name",max_length=20,
                            validators=[MinLengthValidator(2), only_leters])
    image_url = models.URLField(verbose_name="Image URL")
    description = models.TextField(verbose_name="Description",)
    price = models.FloatField(verbose_name="Price")