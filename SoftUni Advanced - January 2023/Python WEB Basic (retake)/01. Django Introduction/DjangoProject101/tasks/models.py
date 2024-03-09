from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=30, null=False) #varchar(30), NOT NULL
    description = models.TextField()
    priority = models.IntegerField()

