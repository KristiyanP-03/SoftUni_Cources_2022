from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.db import models

# Create your models here.
def only_letters(input):
    for letter in input:
        if not letter.isalpha():
            raise ValidationError("The name should contain only letters!")

def at_least_one_digit(input):
    count_of_digits = 0
    for char in input:
        if char.isdigit():
            count_of_digits += 1
    if count_of_digits == 0:
        raise ValidationError("The password must contain at least 1 digit!")



class ProfileModel(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=20, validators=[only_letters])
    last_name = models.CharField(verbose_name="Last Name", max_length=30, validators=[MinLengthValidator(4)])
    email = models.EmailField(verbose_name="Email", max_length=45)
    profile_picture = models.URLField(verbose_name="Profile Picture", blank=True, null=True)
    password = models.CharField(verbose_name="Password", max_length=20, validators=[MinLengthValidator(5), at_least_one_digit])









def valid_date(value):
    if value < timezone.now().date():
        raise ValidationError('The date cannot be in the past!')


class EventModel(models.Model):
    EVENT_CATEGORIES = [
        ('Sports', 'Sports'),
        ('Festivals', 'Festivals'),
        ('Conferences', 'Conferences'),
        ('Performing Art', 'Performing Art'),
        ('Concerts', 'Concerts'),
        ('Theme Party', 'Theme Party'),
        ('Other', 'Other'),
    ]

    event_name = models.CharField(verbose_name="Event Name", max_length=30, validators=[MinLengthValidator(2)])
    category = models.CharField(verbose_name="Category", choices=EVENT_CATEGORIES)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    date = models.DateField(verbose_name="Date", validators=[valid_date])
    event_image = models.URLField(verbose_name="Event Image")
