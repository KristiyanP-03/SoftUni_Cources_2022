# Generated by Django 4.2.3 on 2023-08-10 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FoodieHaven_app', '0003_reportusermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipemodel',
            name='total_rating',
            field=models.PositiveIntegerField(default=0, verbose_name='Total Rating Score'),
        ),
        migrations.CreateModel(
            name='RecipeRatingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Rating')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodieHaven_app.recipemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
