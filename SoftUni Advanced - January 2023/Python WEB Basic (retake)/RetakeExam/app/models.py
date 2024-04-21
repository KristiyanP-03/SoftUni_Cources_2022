from django.db import models

from django.core.exceptions import ValidationError

from django.core.validators import MinValueValidator, MinLengthValidator


# Create your models here.


def validate_nickname(value):
    if len(value) < 2:
        raise ValidationError("Nickname must be at least 2 characters long!")


def validate_name_start_with_capital(value):
    if not value[0].isupper():
        raise ValidationError("Name must start with a capital letter!")


class Profile(models.Model):
    nickname = models.CharField(
        verbose_name="Nickname", null=False, blank=False,
        unique=True, max_length=20,
        validators=[validate_nickname],
    )
    first_name = models.CharField(
        verbose_name="First Name", null=False, blank=False,
        max_length=30,
        validators=[validate_name_start_with_capital],
    )
    last_name = models.CharField(
        verbose_name="Last Name", null=False, blank=False,
        max_length=30,
        validators=[validate_name_start_with_capital],
    )
    chef = models.BooleanField(
        verbose_name="Chef", null=False, blank=False,
        default=False,
    )
    bio = models.TextField(
        verbose_name="Bio", blank=True, null=True
    )


class Recipe(models.Model):
    CHOICES = [
        ('French', 'French'),
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
        ('Balkan', 'Balkan'),
        ('Other', 'Other'),
    ]

    title = models.CharField(
        verbose_name="Title", null=False, blank=False,
        unique=True,
        max_length=100,
        validators=[MinLengthValidator(10)],
    )
    cuisine_type = models.CharField(
        verbose_name="Cuisine Type", null=False, blank=False,
        max_length=7, choices=CHOICES,
    )
    ingredients = models.TextField(
        verbose_name="Ingredients", null=False, blank=False,
        help_text="Ingredients must be separated by a comma and space.",
    )
    instructions = models.TextField(
        verbose_name="Instructions", null=False, blank=False,
    )
    cooking_time = models.PositiveIntegerField(
        verbose_name="Cooking Time", null=False, blank=False,
        validators=[MinValueValidator(1)],
        help_text="Provide the cooking time in minutes.",
    )
    image_url = models.URLField(
        verbose_name="Image URL", blank=True, null=True
    )
