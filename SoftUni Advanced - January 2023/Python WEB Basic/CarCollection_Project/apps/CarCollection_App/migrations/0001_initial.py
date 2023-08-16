# Generated by Django 4.2.4 on 2023-08-15 13:56

import apps.CarCollection_App.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Sports Car', 'Sports Car'), ('Pickup', 'Pickup'), ('Crossover', 'Crossover'), ('Minibus', 'Minibus'), ('Other', 'Other')], verbose_name='Type')),
                ('model', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Model')),
                ('year', models.IntegerField(validators=[apps.CarCollection_App.models.year_range], verbose_name='Year')),
                ('image_url', models.URLField(verbose_name='Image Url')),
                ('price', models.FloatField(validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[apps.CarCollection_App.models.min_username_length], verbose_name='Username')),
                ('emails', models.EmailField(max_length=254, verbose_name='Email')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18)], verbose_name='Age')),
                ('password', models.CharField(max_length=30, verbose_name='Password')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Last Name')),
                ('profile_picture', models.URLField(blank=True, null=True, verbose_name='Profile Picture')),
            ],
        ),
    ]