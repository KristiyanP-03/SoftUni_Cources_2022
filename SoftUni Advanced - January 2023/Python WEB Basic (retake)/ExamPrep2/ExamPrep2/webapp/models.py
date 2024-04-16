from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.
def letters_numbers_underscores_only_validator(value):
    for char in value:
        if not (char.isnumeric() or char.isalpha() or char == "_"):
            raise ValidationError("Ensure this value contains only letters, numbers, and underscores.")


class Profile(models.Model):
    username = models.CharField(
        verbose_name="Username",
        max_length=15,
        null=False, blank=False,
        validators=[
            MinLengthValidator(2),
            letters_numbers_underscores_only_validator,
        ],
    )

    email = models.EmailField(
        verbose_name="Email",
        null=False, blank=False,
    )

    age = models.PositiveIntegerField(
        verbose_name="Age",
        null=True, blank=True,
    )


class Album(models.Model):
    GENRE_TYPE = (
        ("pop", "Pop Music"),
        ("jazz", "Jazz Music"),
        ("rnb", "R&B Music"),
        ("rock", "Rock Music"),
        ("country", "Country Music"),
        ("dance", "Dance Music"),
        ("hiphop", "Hip Hop Music"),
        ("other", "Other")
    )

    album_name = models.CharField(
        verbose_name="Album Name",
        null=False, blank=False,
        unique=True,
        max_length=30,
    )

    artist = models.CharField(
        verbose_name="Artist",
        null=False, blank=False,
        max_length=30,
    )

    genre = models.CharField(
        verbose_name="Genre",
        null=False, blank=False,
        max_length=30,
        choices=GENRE_TYPE,
    )

    description = models.TextField(
        verbose_name="Description",
        null=True, blank=True,
    )

    imageURL = models.URLField(
        verbose_name="image URL",
        null=False, blank=False,
    )

    price = models.FloatField(
        verbose_name="Price",
        null=False, blank=False,
        validators=[
            MinValueValidator(0.0)
        ]
    )
