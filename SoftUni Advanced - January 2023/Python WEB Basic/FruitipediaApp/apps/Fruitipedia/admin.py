from django.contrib import admin

from apps.Fruitipedia.models import ProfileModel, FruitModel


# Register your models here.
@admin.register(ProfileModel)
class Profiles(admin.ModelAdmin):
    pass

@admin.register(FruitModel)
class Fruits(admin.ModelAdmin):
    pass
