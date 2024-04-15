from django.core.validators import *
from django.db import models


# Create your models here.
def validate_string(value):
    if not re.match(r'^[A-Za-z0-9_]*$', value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscores.")

class Profile(models.Model):
    USERNAME_MIN_LENGTH = 2
    USERNAME_MAX_LENGTH = 15

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        null=False, blank=False,  # to be required
        validators=MinLengthValidator(
            USERNAME_MIN_LENGTH,
            validate_string
        ),  # validator for min length
    )

    email = models.EmailField(
        null=False, blank=False,
    )

    age = models.PositiveIntegerField(
        null=True, blank=True,
    )

class Album(models.Model):
    pass
