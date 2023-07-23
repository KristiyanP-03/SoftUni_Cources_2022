from django.core import validators
from django.db import models

# Create your models here.
class GameModel(models.Model):
    CATEGORY_CHOICES = (("Action", "Action"), ("Adventure", "Adventure"),
                        ("Puzzle", "Puzzle"), ("Strategy","Strategy"),
                        ("Sports", "Sports"), ("Board/Card Game", "Board/Card Game"),
                        ("Other", "Other"))

    title = models.CharField(verbose_name="Title", unique="True", max_length=30)
    category = models.CharField(verbose_name="Category", max_length=15, choices=CATEGORY_CHOICES)
    rating = models.FloatField(verbose_name="Rating",
                               validators=[validators.MinValueValidator(0.1), validators.MaxValueValidator(5.0)])
    max_level = models.IntegerField(verbose_name="Max Level",
                                    blank=True, null=True, validators=[validators.MinValueValidator(1)])
    image_url = models.URLField(verbose_name="Image URL")
    summary = models.TextField(verbose_name="Summary",  blank=True, null=True)