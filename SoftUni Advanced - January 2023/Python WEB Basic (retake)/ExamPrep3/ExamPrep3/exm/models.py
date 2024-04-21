from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


# Create your models here.
def validate_username(value):
    if len(value) < 3:
        raise ValidationError("Username must be at least 3 characters long!")
    for char in value:
        if not (char.isnumeric() or char.isalpha() or char == "_"):
            raise ValidationError("Ensure this value contains only letters, numbers, and underscores.")


def validate_year(value):
    if value < 1999 or value > 2030:
        raise ValidationError("Year must be between 1999 and 2030!")


def validate_unique_image_url(value):
    if Car.objects.filter(image_url=value).exists():
        raise ValidationError("This image URL is already in use! Provide a new one.")


class Profile(models.Model):
    username = models.CharField(
        verbose_name="Username", blank=False, null=False,
        max_length=15, validators=[validate_username],
    )
    email = models.EmailField(
        verbose_name="Email", blank=False, null=False,
    )
    age = models.IntegerField(
        verbose_name="Age", blank=False, null=False,
        help_text="Age requirement: 21 years and above",
    )
    password = models.CharField(
        verbose_name="Password", blank=False, null=False,
        max_length=20,
    )
    first_name = models.CharField(
        verbose_name="First Name", blank=True, null=True,
        max_length=25,
    )
    last_name = models.CharField(
        verbose_name="Last Name", blank=True, null=True,
        max_length=25,
    )
    profile_picture = models.URLField(
        verbose_name="Profile Picture", blank=True, null=True,
    )


class Car(models.Model):
    TYPE_CHOICES = [
        ('Rally', 'Rally'),
        ('Open-wheel', 'Open-wheel'),
        ('Kart', 'Kart'),
        ('Drag', 'Drag'),
        ('Other', 'Other')
    ]
    type = models.CharField(
        verbose_name="Type", blank=False, null=False,
        max_length=10, choices=TYPE_CHOICES,
    )
    model = models.CharField(
        verbose_name="Model", blank=False, null=False,
        max_length=15
    )
    year = models.IntegerField(
        verbose_name="Year", blank=False, null=False,
        validators=[validate_year],
    )
    image_url = models.URLField(
        verbose_name="Image URL", blank=False, null=False,
        unique=True, default="https://...",
        validators=[validate_unique_image_url],
    )
    price = models.FloatField(
        verbose_name="Price", blank=False, null=False,
        validators=[MinValueValidator(1.0)],
    )
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='cars', editable=False, verbose_name="Owner"
    )
