from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField("Put your first name here", max_length=30)
    last_name = models.CharField("Put your last name here", max_length=30)
    email_address = models.EmailField(unique=True)
    works_full_time = models.BooleanField(default=True)
    job_level = models.CharField(max_length=20)
    photo = models.URLField(
        default='https://cdn.discordapp.com/emojis/1099197034696810516.gif?size=96&quality=lossless', blank=True)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"