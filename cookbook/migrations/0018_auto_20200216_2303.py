# Generated by Django 3.0.2 on 2020-02-16 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0017_auto_20200216_2257'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipeIngredients',
            new_name='RecipeIngredient',
        ),
    ]
