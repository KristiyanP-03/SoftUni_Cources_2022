from django.core import validators
from django.db import models

# Create your models here.
class ProfileModel(models.Model):

    email = models.EmailField(verbose_name="Email")
    age = models.IntegerField(verbose_name="Age", validators=[validators.MinValueValidator(12)])
    password = models.CharField(verbose_name="Password", max_length=30)
    first_name = models.CharField(verbose_name="First Name", blank=True, null=True, max_length=30)
    last_name = models.CharField(verbose_name="Last Name", blank=True, null=True, max_length=30)
    profile_picture = models.URLField(verbose_name="Profile Picture", blank=True, null=True)

