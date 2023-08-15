from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

# Create your models here.
def min_username_length(input):
    if len(input) < 2:
        raise ValidationError("The username must be a minimum of 2 chars")



class ProfileModel(models.Model):
    username = models.CharField(verbose_name="Username", max_length=10, validators=[min_username_length])
    email = models.EmailField(verbose_name="Email")
    age = models.IntegerField(verbose_name="Age", validators=[MinValueValidator(18)])
    password = models.CharField(verbose_name="Password", max_length=30)
    first_name = models.CharField(verbose_name="First Name", max_length=30, blank=True, null=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=30, blank=True, null=True)
    profile_picture = models.URLField(verbose_name="Profile Picture", blank=True, null=True)


#======================================================================================================



def year_range(input):
    if not 1980 <= input <= 2049:
        raise ValidationError("Year must be between 1980 and 2049")


class CarModel(models.Model):
    CAR_TYPE = (
        ("Sports Car", "Sports Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other"),
    )

    type = models.CharField(verbose_name="Type", choices=CAR_TYPE)
    model = models.CharField(verbose_name="Model", max_length=20, validators=[MinLengthValidator(2)])
    year = models.IntegerField(verbose_name="Year", validators=[year_range])
    image_url = models.URLField(verbose_name="Image Url")
    price = models.FloatField(verbose_name="Price", validators=[MinValueValidator(1)])




